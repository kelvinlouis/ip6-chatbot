from pymongo import MongoClient
import datetime
import os
import shutil
import zipfile

class ConversationLogger:
    def __init__(self, mongo_url, mongo_db, enabled = False):
        self.db_name = mongo_db
        self.db_url = mongo_url
        self.db_collection_name = "conversations"
        self.enabled = enabled
        self.conversation_id = None
        self.participant_id = None

        # Establishes and saves mongo db connection
        self._client = MongoClient(mongo_url)
        self._db = self._client[self.db_name]
        self._conversations = self._db[self.db_collection_name]

    # Creates a conversation document and stores it in the collection 
    def create_conversation(self, conversation_id, participant_id):
        if self.enabled == False:
            return

        self.conversation_id = conversation_id
        self.participant_id = participant_id

        conversation = {
            "conversation_id": conversation_id,
            "participant_id": participant_id,
            "messages": []
        }

        self._conversations.insert_one(conversation)

    # Logs a message sent by the user
    def log_user_sent_message(self, text):
        if self._can_log() == False:
            return

        message = self._create_message("user_sent_message", "User", text)
        self._add_message(message)

    # Logs a message corrected by the user
    def log_user_corrected_message(self, text):
        if self._can_log() == False:
            return

        message = self._create_message("user_corrected_message", "User", text)
        self._add_message(message)

    # Logs a message sent by the bot
    def log_bot_sent_message(self, text):
        if self._can_log() == False:
            return

        message = self._create_message("bot_sent_message", "Bot", text)
        self._add_message(message)
    
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

            file = open("temp/text/{}.txt".format(conversation["participant_id"]), "w")
            
            for message in conversation["messages"]:
                file.write("[{}] {}: {}\n".format(message["date"].strftime("%Y-%m-%d %H:%M"), message["author"], message["text"]))

            file.close()
        
        # Create zip
        zip_name = "temp/conversations"
        shutil.make_archive(zip_name, 'zip', "temp/text")

        return os.path.abspath(zip_name + ".zip")


    # In order to log, it must be enabled and a conversation had to be created
    def _can_log(self):
        return self.enabled == True and self.conversation_id != None and self.participant_id != None

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
    
    # Finds a conversation based on the conversation id
    def _get_conversation(self, conversation_id):
        return self._conversations.find_one({ "conversation_id": conversation_id })
