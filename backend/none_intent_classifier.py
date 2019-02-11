from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import map
from typing import Any
from typing import Dict
from typing import Text

import logging

from rasa_nlu.components import Component
from rasa_nlu.training_data import Message

logger = logging.getLogger(__name__)

class NoneIntentClassifier(Component):
    """
    This is a custom component for the NLU pipeline.
    RASA NLU has issues identifying an intent if just a word or two are mentioned.
    This component ensures that the correct intent is mapped, if it detected a certain entity.
    Examples: '200 people' -> provide_nr_of_people, 'Mark' -> provide_name
    """
    
    name = "intent_classifier_none"

    provides = ["intent"]

    requires = ["intent", "entities"]

    def __init__(self, component_config=None):
        super(NoneIntentClassifier, self).__init__(component_config)

    def process(self, message, **kwargs):
        # type: (Message, **Any) -> None

        substitution_rules = [
            {
                "entity": ["name"],
                "intent": "provide_name"
            },
            {
                "entity": ["company", "name"],
                "intent": "provide_name"
            },
            {
                "entity": ["date"],
                "intent": "provide_booking_date"
            },
            {
                "entity": ["time"],
                "intent": "provide_booking_date"
            },
            {
                "entity": ["date", "time"],
                "intent": "provide_booking_date"
            },
            {
                "entity": ["nr_of_people"],
                "intent": "provide_nr_of_people"
            },
            {
                "entity": ["budget"],
                "intent": "provide_budget"
            },
            {
                "entity": ["start_location"],
                "intent": "provide_booking_date"
            },
            {
                "entity": ["room"],
                "intent": "provide_room"
            }
        ]

        entities = message.get("entities", [])[:]
        current_intent = message.get("intent", [])

        logger.debug("current_intent: {}".format(current_intent))

        if current_intent["name"] == None:         
            found_entities = []
            for entity in entities:
                found_entities.append(entity["entity"])

            found_entities.sort()
            
            for substitution_rule in substitution_rules:
                if substitution_rule["entity"] == found_entities:
                        corrected_intent = {"name": substitution_rule["intent"], "confidence": 1.0}
                        message.set("intent", corrected_intent, add_to_output=True)
                        logger.debug("corrected_intent: {}".format(corrected_intent))
                    