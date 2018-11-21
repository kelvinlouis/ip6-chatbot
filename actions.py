from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionCorrectRoom(Action):
   def name(self):
      # type: () -> Text
      return "action_correct_room"

   def run(self, dispatcher, tracker, domain):
      current_room = tracker.get_slot('current_room')
      room = tracker.get_slot('room')
      room = room.lower()

      if room == 'alpha' or room == 'first':
        return [SlotSet('current_room', 'Alpha'), SlotSet('room', None)]
      elif room == 'beta' or room == 'second':
        return [SlotSet('current_room', 'Beta'), SlotSet('room', None)]
      elif room == 'gamma' or room == 'third' or room == 'last':
        return [SlotSet('current_room', 'Gamma'), SlotSet('room', None)]
      
      return [SlotSet('room', None)]
