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

logger = logging.getLogger(__name__)


class WebappBlueprint(Blueprint):
    def __init__(self, sio, socketio_path, *args, **kwargs):
        self.sio = sio
        self.socketio_path = socketio_path
        super(WebappBlueprint, self).__init__(*args, **kwargs)

    def register(self, app, options, first_registration=False):
        app.wsgi_app = socketio.Middleware(self.sio, app.wsgi_app,
                                           self.socketio_path)
        super(WebappBlueprint, self).register(app, options, first_registration)


class WebappOutput(OutputChannel):

    @classmethod
    def name(cls):
        return "webapp"

    def __init__(self, sio, bot_message_evt, conversation_logger):
        self.sio = sio
        self.bot_message_evt = bot_message_evt
        self.conversation_logger = conversation_logger

    def send(self, recipient_id: Text, message: Any) -> None:
        """Sends a message to the recipient."""
        self.sio.emit(message, room=recipient_id)

    def _send_message(self, recipient_id: Text, response: Any) -> None:
        """Sends a message to the recipient using the bot event."""
        self.sio.emit(self.bot_message_evt, response, room=recipient_id)

    def send_text_message(self, recipient_id: Text, message: Text) -> None:
        """Send a message through this channel."""
        self.conversation_logger.bot_sent_message(message)
        self._send_message(recipient_id, {"text": message})


class WebappInput(InputChannel):
    """A webapp input channel."""

    @classmethod
    def name(cls):
        return "webapp"

    @classmethod
    def from_credentials(cls, credentials):
        credentials = credentials or {}
        return cls(credentials.get("user_message_evt", "user_uttered"),
                   credentials.get("bot_message_evt", "bot_uttered"),
                   credentials.get("namespace"),
                   credentials.get("logger_enabled", False),
                   credentials.get("mongodb_url", "localhost"),
                   credentials.get("mongodb_db", "chatbot"))

    def __init__(self,
                 user_message_evt: Text = "user_uttered",
                 bot_message_evt: Text = "bot_uttered",
                 namespace: Optional[Text] = None,
                 logger_enabled = False,
                 mongodb_url: Text = "localhost",
                 mongodb_db: Text = "chatbot",
                 socketio_path='/socket.io'  # type: Optional[Text]
                 ):
        self.bot_message_evt = bot_message_evt
        self.user_message_evt = user_message_evt
        self.namespace = namespace
        self.socketio_path = socketio_path
        self.conversation_logger_manager = ConversationLoggerManager(mongodb_url, mongodb_db, logger_enabled)

    def blueprint(self, on_new_message):
        sio = socketio.Server()
        socketio_webhook = WebappBlueprint(sio, self.socketio_path,
                                           'socketio_webhook', __name__)

        @socketio_webhook.route("/", methods=['GET'])
        def health():
            return jsonify({"status": "ok"})

        @socketio_webhook.route("/export", methods=['GET'])
        def export():
            attachment_filename = "conversations_{}.zip".format(
                datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
            zip_filename = self.conversation_logger_manager.export()
            return send_file(zip_filename, mimetype="application/zip", attachment_filename=attachment_filename, as_attachment=True)

        @sio.on('connect', namespace=self.namespace)
        def connect(sid, environ):
            logger.debug("User {} connected to socketio endpoint.".format(sid))

        @sio.on('disconnect', namespace=self.namespace)
        def disconnect(sid):
            logger.debug("User {} disconnected from socketio endpoint."
                         "".format(sid))
        
        @sio.on(self.user_message_evt, namespace=self.namespace)
        def handle_message(sid, data):
            participant_id = data['participant_id']
            user_text = data['message']

            logger = self.conversation_logger_manager.create(sid, participant_id)

            # No logger will be created, if it is not enabled
            logger.user_sent_message(user_text)

            output_channel = WebappOutput(
                sio, self.bot_message_evt, logger)
            message = UserMessage(user_text, output_channel, sid,
                                  input_channel=self.name())
            on_new_message(message)

        return socketio_webhook
