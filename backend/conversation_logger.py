from pymongo import MongoClient
import datetime
import os
import shutil
import zipfile

'''
    The manager is responsible for creating an individual logger per request,
    in order to keep the logger stateless.
    Every logger gets a db connection and the necessary ids.
'''
class ConversationLoggerManager:
    def __init__(self, mongo_url, mongo_username, mongo_password, mongo_database, enabled=False):
        self.enabled = enabled

        # Establishes and saves mongo db connection
        if mongo_username == None and mongo_password == None:
            self._client = MongoClient(mongo_url)
        else:
            self._client = MongoClient(mongo_url, username=mongo_username, password=mongo_password)

        self._db = self._client[mongo_database]
        self._conversations = self._db["conversations"]

    # Creates an instance of a logger
    def create(self, conversation_id, participant_id):
        if self.enabled == False:
            return ConversationDummyLogger()

        return ConversationLogger(
            self._db, self._conversations, conversation_id, participant_id)
    
    # Creates a txt file for every conversation and zips it
    def export(self):
        # Remove previously created temporary files
        shutil.rmtree("temp/", ignore_errors=True)

        conversations = self._conversations.find()

        # Creates the directories
        os.makedirs("temp/text", exist_ok=True)

        # Creates a txt file for every conversation
        for conversation in conversations:
            if len(conversation["messages"]) == 0:
                continue

            file = open("temp/text/{}.txt".format(conversation["participant_id"]), "a")

            for message in conversation["messages"]:
                file.write("[{}] {}: {}\n".format(message["date"].strftime(
                    "%Y-%m-%d %H:%M"), message["author"], message["text"]))
            
            file.write("\n\n")
            file.close()

        # Create zip
        zip_name = "temp/conversations"
        shutil.make_archive(zip_name, 'zip', "temp/text")

        return os.path.abspath(zip_name + ".zip")

'''
    This logger stores the messages of the bot and the user of a participant.
    Messages are logged/stored in a mongo database. If logging is enabled,
    instances of it will be created by the manager.
'''
class ConversationLogger:
    def __init__(self, db, conversations, conversation_id, participant_id):
        self._db = db
        self._conversations = conversations

        # Stores the ids of a conversation
        self.conversation_id = conversation_id
        self.participant_id = participant_id
        
        # Creates a document in the database
        self._create_document()

    # Logs a message sent by the user
    def user_sent_message(self, text):
        message = self._create_message("user_sent_message", "User", text)
        self._add_message(message)

    # Logs a message corrected by the user
    def user_corrected_message(self, text):
        message = self._create_message("user_corrected_message", "User", text)
        self._add_message(message)

    # Logs a message sent by the bot
    def bot_sent_message(self, text):
        message = self._create_message("bot_sent_message", "Bot", text)
        self._add_message(message)

    # Creates a message document
    def _create_message(self, message_type, author, text):
        message = {
            "type": message_type,
            "author": author,
            "text": text,
            "date": datetime.datetime.utcnow()
        }

        return message
    
    # Appends the received message to the conversation document 
    def _add_message(self, message):
        self._conversations.update(
            { "conversation_id": self.conversation_id },
            { "$push": { "messages": message } }
        )
    
    # Creates a conversation document and stores it in the collection
    def _create_document(self):
        count = self._conversations.count_documents({
            "conversation_id": self.conversation_id,
            "participant_id": self.participant_id
        })

        if count == 0:
            # Creates the document
            conversation = {
                "conversation_id": self.conversation_id,
                "participant_id": self.participant_id,
                "messages": []
            }

            self._conversations.insert_one(conversation)

'''
    Functions as a dummy/empty logger, so clients of the logger
    do not have to worry if logging is enabled or not.
    This is used if logging is disabled.
'''
class ConversationDummyLogger:
    def __init__(self):
        ''''''

    def user_sent_message(self, text):
        ''''''

    def user_corrected_message(self, text):
        ''''''

    def bot_sent_message(self, text):
        ''''''
