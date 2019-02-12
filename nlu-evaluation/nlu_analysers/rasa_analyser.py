from luis_analyser import *

class RasaAnalyser(LuisAnalyser):
	def __init__(self, rasa_url, project):
		super(LuisAnalyser, self).__init__()
		self.project = project
		self.url = rasa_url + "?q=%s&project=%s"
