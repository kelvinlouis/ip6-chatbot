import logging
import datetime
from typing import Optional, Text, Any, List, Dict

import socketio
from flask import Blueprint, jsonify, send_file

from rasa_core.channels import InputChannel
from rasa_core.channels.channel import (
    UserMessage,
    OutputChannel)

from conversation_logger import ConversationLoggerManager
from languagetool.api import LanguageToolApi
from nlu.api import NluApi

logger = logging.getLogger(__name__)


class WebappBlueprint(Blueprint):
    """Registers flask middleware, in order to intercept socket.io messages."""
    def __init__(self, sio, socketio_path, *args, **kwargs):
        self.sio = sio
        self.socketio_path = socketio_path
        super(WebappBlueprint, self).__init__(*args, **kwargs)

    def register(self, app, options, first_registration=False):
        app.wsgi_app = socketio.Middleware(self.sio, app.wsgi_app,
                                           self.socketio_path)
        super(WebappBlueprint, self).register(app, options, first_registration)


class WebappOutput(OutputChannel):
    """
    This class is used for outbound socket communication with the user.
    It exposes methods that are invoked once the chatbot (RASA core) constructed a response.
    """
    @classmethod
    def name(cls):
        return "webapp"

    def __init__(self, sio, bot_message_evt, conversation_logger, language_errors):
        self.sio = sio

        # Types of socket.io events
        self.bot_found_errors_evt = "bot_found_errors"
        self.bot_message_evt = bot_message_evt
        
        # Used to log messages of the bot
        self.conversation_logger = conversation_logger

        # A list of errors found by language tool
        self.language_errors = language_errors

    def send(self, recipient_id: Text, message: Any) -> None:
        """Sends a message to the recipient."""
        self.sio.emit(message, room=recipient_id)

    def send_text_message(self, recipient_id: Text, message: Text) -> None:
        """Send a message through this channel."""
        self.conversation_logger.bot_sent_message(message)
        self._send_message(recipient_id, {"text": message})
    
    def send_language_errors(self, recipient_id: Text, message_id: Text, errors: Any) -> None:
        """Sends a list of language errors that were detected."""
        self.sio.emit(self.bot_found_errors_evt, {"messageId": message_id, "errors": errors}, room=recipient_id)

    def _send_message(self, recipient_id: Text, response: Any) -> None:
        """Sends a message to the recipient using the bot event."""
        self.sio.emit(self.bot_message_evt, response, room=recipient_id)

class WebappInput(InputChannel):
    """
    This class is responsible for incomming requests received by
    the socket.io and rest endpoints. The socket.io endpoints receives
    chat messages from the user. The REST endpoints are used for administrative purposes.
    """

    @classmethod
    def name(cls):
        return "webapp"

    @classmethod
    def from_credentials(cls, credentials):
        """Receives the credentials from the credentials.yml file"""
        credentials = credentials or {}
        return cls(credentials.get("user_message_evt", "user_uttered"),
                   credentials.get("bot_message_evt", "bot_uttered"),
                   credentials.get("namespace"),
                   credentials.get("logger_enabled", False),
                   credentials.get("nlu_url", "localhost"),
                   credentials.get("nlu_port", 5000),
                   credentials.get("nlu_project", "default"),
                   credentials.get("nlu_model", "test"),
                   credentials.get("languagetool_enabled", False),
                   credentials.get("languagetool_url", "localhost"),
                   credentials.get("languagetool_port", 8080),
                   credentials.get("mongodb_url", "localhost"),
                   credentials.get("mongodb_username", None),
                   credentials.get("mongodb_password", None),
                   credentials.get("mongodb_database", "chatbot"))

    def __init__(self,
                 user_message_evt: Text = "user_uttered",
                 bot_message_evt: Text = "bot_uttered",
                 namespace: Optional[Text] = None,
                 logger_enabled: bool = False,
                 nlu_url: Text = "localhost",
                 nlu_port: int = 5000,
                 nlu_project: Text = "default",
                 nlu_model: Text = "test",
                 languagetool_enabled: bool = False,
                 languagetool_url: Text = "localhost",
                 languagetool_port: int = 8080,
                 mongodb_url: Text = "localhost",
                 mongodb_username: Text = None,
                 mongodb_password: Text = None,
                 mongodb_database: Text = "chatbot",
                 socketio_path="/socket.io"  # type: Optional[Text]
                 ):
        self.bot_message_evt = bot_message_evt
        self.user_message_evt = user_message_evt
        self.namespace = namespace
        self.socketio_path = socketio_path
        self.conversation_logger_manager = ConversationLoggerManager(
            mongodb_url, mongodb_username, mongodb_password, 
            mongodb_database, logger_enabled)
        self.languagetool_enabled = languagetool_enabled
        if languagetool_enabled:
            self.languagetool_api = LanguageToolApi(languagetool_url, languagetool_port)
        self.nlu_api = NluApi(nlu_url, nlu_port, nlu_project, nlu_model)

    def blueprint(self, on_new_message):
        sio = socketio.Server()
        socketio_webhook = WebappBlueprint(sio, self.socketio_path,
                                           "socketio_webhook", __name__)

        @socketio_webhook.route("/", methods=["GET"])
        def health():
            """A simple check to see if the service is running."""
            return jsonify({"status": "ok"})

        @socketio_webhook.route("/export", methods=["GET"])
        def export():
            """Endpoint exposing an export to retrieve all stored conversations."""
            attachment_filename = "conversations_{}.zip".format(
                datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
            zip_filename = self.conversation_logger_manager.export()
            return send_file(zip_filename, mimetype="application/zip", attachment_filename=attachment_filename, as_attachment=True)

        @sio.on("connect", namespace=self.namespace)
        def connect(sid, environ):
            logger.debug("User {} connected to socketio endpoint.".format(sid))

        @sio.on("disconnect", namespace=self.namespace)
        def disconnect(sid):
            logger.debug("User {} disconnected from socketio endpoint."
                         "".format(sid))
        
        @sio.on(self.user_message_evt, namespace=self.namespace)
        def handle_message(sid, data):
            """Called whenever the socket receives a message from the user."""
            participant_id = data["participant_id"]
            user_text = data["message"]
            message_id = data["message_id"]

            # Creates an instance of the conversational logger and logs message
            conversation_logger = self.conversation_logger_manager.create(sid, participant_id)
            conversation_logger.user_sent_message(user_text)
            
            language_errors = []
            lt_response = None

            if self.languagetool_enabled:
                try:
                    # Extract entities from the message
                    nlu_response = self.nlu_api.parse(user_text)
                    nlu_entities = nlu_response["entities"]

                    # Check if text contains error
                    lt_response = self.languagetool_api.check(user_text)

                    # Ignore hesitation errors and errors that are entities
                    lt_response.ignore_hesitation_errors()
                    lt_response.ignore_entity_errors(nlu_entities, ["name"])
                    language_errors = lt_response.errors_to_dict()
                except (TypeError, ValueError):
                    logger.debug("Error occurred using LanguageTool")

            output_channel = WebappOutput(
                sio, self.bot_message_evt, conversation_logger, language_errors)

            if len(language_errors) > 0:
                # Send found errors to the client
                output_channel.send_language_errors(
                    sid, message_id, language_errors)

            if lt_response != None and lt_response.error_ratio() >= 0.25:
                # Circumvent the chatbot if the ratio is to high
                output_channel.send_text_message(
                    sid, "I am afraid I have trouble understanding. Please could you rephrase?")
            else:
                # No error found, pass user message to bot
                message = UserMessage(
                    user_text, output_channel, sid, input_channel=self.name())

                on_new_message(message)

        return socketio_webhook
