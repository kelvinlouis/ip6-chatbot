import requests
import re

class NluApi:
    """A service to communicate with the NLU server."""

    def __init__(self, server_url, server_port, project, model, verbose=False):
        self.api_url = "http://{}:{}".format(server_url, server_port)
        self.project = project
        self.model = model
        self.verbose = verbose

    def parse(self, input_text):
        """
        Calls the parse endpoint, which detects the intent and entities of a message.
        """
        url = self.api_url + "/parse"

        payload = {
            "project": self.project,
            "model": self.model,
            "q": input_text,
        }

        response = requests.post(url, json=payload)

        if response.status_code != 200:
            raise ValueError(response.text)
        
        response_body = response.json()

        if self.verbose:
            print(request_parameters)
            print(response_body)

        return response_body
