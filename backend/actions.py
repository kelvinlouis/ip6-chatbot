from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionCorrectRoom(Action):
   def name(self):
      # type: () -> Text
      return "action_correct_room"

   def run(self, dispatcher, tracker, domain):
      current_room = tracker.get_slot('current_room')
      room = tracker.get_slot('room')

      if room != None:
        room = room.lower()

        if room == 'alpha' or room == 'first':
          return [SlotSet('current_room', 'Alpha'), SlotSet('room', None)]
        elif room == 'beta' or room == 'second':
          return [SlotSet('current_room', 'Beta'), SlotSet('room', None)]
        elif room == 'gamma' or room == 'third' or room == 'last':
          return [SlotSet('current_room', 'Gamma'), SlotSet('room', None)]
      
      return [SlotSet('room', None)]

class ActionSetTopic(Action):
   def name(self):
      # type: () -> Text
      return "action_set_topic"

   def run(self, dispatcher, tracker, domain):
      intent = tracker.latest_message['intent'].get('name')

      if intent != None:
        if intent == 'ask_for_room_atmosphere':
          return [SlotSet('topic', 'atmosphere')]
        elif intent == 'ask_for_room_lighting':
          return [SlotSet('topic', 'lighting')]
        elif intent == 'ask_for_room_equipment':
          return [SlotSet('topic', 'equipment')]
        elif intent == 'ask_for_room_highlight':
          return [SlotSet('topic', 'highlight')]
        elif intent == 'ask_for_room_price':
          return [SlotSet('topic', 'price')]
        elif intent == 'ask_for_room_seating':
          return [SlotSet('topic', 'seating')]
        elif intent == 'ask_for_room_size':
          return [SlotSet('topic', 'size')]

      return []
