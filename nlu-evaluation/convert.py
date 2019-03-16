from nlu_converters.luis_converter import LuisConverter
from nlu_converters.rasa_luis_converter import RasaLuisConverter
from nlu_converters.dialogflow_converter import DialogflowConverter

# LUIS and Rasa
luis_converter = RasaLuisConverter()
luis_converter.import_corpus("data/raw/ip6_corpus.json")
luis_converter.export("data/converted/ip6_corpus_LUIS.json")

# Dialogflow
dialogflow_converter = DialogflowConverter()
dialogflow_converter.import_corpus("data/raw/ip6_corpus.json")
dialogflow_converter.export("data/converted/ip6_corpus_Dialogflow.zip")