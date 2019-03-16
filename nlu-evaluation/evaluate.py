from nlu_analysers.dialogflow_analyser import DialogflowAnalyser
from nlu_analysers.luis_analyser import LuisAnalyser
from nlu_analysers.rasa_analyser import RasaAnalyser

# Dialogflow
dialogflow_analyser = DialogflowAnalyser("<APIKey>")
dialogflow_analyser.get_annotations("data/raw/ip6_corpus.json", "data/results/ip6_corpus_annotations_dialogflow.json")
dialogflow_analyser.analyse_annotations("data/results/ip6_corpus_annotations_dialogflow.json", "data/raw/ip6_corpus.json", "data/results/ip6_corpus_analysis_dialogflow.json")

# LUIS
luis_analyser = LuisAnalyser("<ApplicationID>", "<SubscriptionID>")
luis_analyser.get_annotations("data/raw/ip6_corpus.json", "data/results/ip6_corpus_annotations_luis.json")
luis_analyser.analyse_annotations("data/results/ip6_corpus_annotations_luis.json", "data/raw/ip6_corpus.json", "data/results/ip6_corpus_analysis_luis.json")

# Rasa
rasa_analyser = RasaAnalyser("<ServerURL>", "<Project>")
rasa_analyser.get_annotations("data/raw/ip6_corpus.json", "data/results/ip6_corpus_annotations_rasa.json")
rasa_analyser.analyse_annotations("data/results/ip6_corpus_annotations_rasa.json", "data/raw/ip6_corpus.json", "data/results/ip6_corpus_analysis_rasa.json")