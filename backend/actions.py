from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionCorrectRoom(Action):
    """
    This action is invoked by RASA core.
    It sets the current room slot to the most recently mentioned room.
    This allows the chatbot to respond to messages containing 'this room',
    because it retains the current room.
    """
    def name(self):
        # type: () -> Text
        return "action_correct_room"

    def run(self, dispatcher, tracker, domain):
        current_room = tracker.get_slot("current_room")
        room = tracker.get_slot("room")

        if room != None:
            room = room.lower()

            if room == "alpha" or room == "first":
                return [SlotSet("current_room", "Alpha"), SlotSet("room", None)]
            elif room == "beta" or room == "second":
                return [SlotSet("current_room", "Beta"), SlotSet("room", None)]
            elif room == "gamma" or room == "third" or room == "last":
                return [SlotSet("current_room", "Gamma"), SlotSet("room", None)]
        
        # Reset the room slot, because current_room is decisive
        return [SlotSet("room", None)]


class ActionSetTopic(Action):
    """
    This action is invoked by RASA core.
    Based on the recent detected event, a topic slot is set
    in order to retain what the user is currently talking about.
    This allows the bot to respond to messages like 'what about the others?'
    The topic slot is a categorical slot.
    """

    def name(self):
        # type: () -> Text
        return "action_set_topic"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message["intent"].get("name")

        if intent != None:
            if intent == "ask_for_room_atmosphere":
                return [SlotSet("topic", "atmosphere")]
            elif intent == "ask_for_room_lighting":
                return [SlotSet("topic", "lighting")]
            elif intent == "ask_for_room_equipment" or intent == "greet+ask_for_room_equipment":
                return [SlotSet("topic", "equipment")]
            elif intent == "ask_for_room_highlight":
                return [SlotSet("topic", "highlight")]
            elif intent == "ask_for_room_price" or intent == "greet+ask_for_room_price":
                return [SlotSet("topic", "price")]
            elif intent == "ask_for_room_seating":
                return [SlotSet("topic", "seating")]
            elif intent == "ask_for_room_size" or intent == "greet+ask_for_room_size":
                return [SlotSet("topic", "size")]

        return []
