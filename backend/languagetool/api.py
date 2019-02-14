import requests
import re

class LanguageError:
    """
    Base class for different error types detected using language tool.
    It contains a reduced set of values, compared to the response of language tool.
    """
    def __init__(self, match):
        text_containing_error = match["context"]["text"]
        self.start_pos = match["offset"]
        self.end_pos = self.start_pos + match["length"]
        self.error = text_containing_error[self.start_pos:self.end_pos]
        self.suggestion = self.extract_suggestion(match)
        self.message = None

    def extract_suggestion(self, match):
        """Only consider the option if one suggestion is mentioned."""
        suggestion = None
        if (len(match["replacements"]) == 1):
            suggestion = match["replacements"][0]["value"]
        
        return suggestion


class LanguageSpellingError(LanguageError):
    """Created when a spelling error is detected."""

    def __init__(self, match):
        LanguageError.__init__(self, match)
        self.type = "spelling"
        self.message = self._generate_message()
    
    def _generate_message(self):
        """If a suggestion was found, integrate it into the message"""
        if self.suggestion != None:
            return "It looks like you misspelled. Did you mean '{}'?".format(
                self.suggestion)
        else:
            return "Misspelled"


class LanguageGrammarError(LanguageError):
    """Represents any type of grammatical error."""

    def __init__(self, match):
        LanguageError.__init__(self, match)
        self.type = "grammar"
        self.message = match["message"]


class LanguageNonConformanceError(LanguageError):
    """Non-conformance errors are detected by the language model (n-grams) of language tool."""

    def __init__(self, match):
        LanguageError.__init__(self, match)
        self.type = "non-conformance"
        self.message = self._generate_message()
    
    def _generate_message(self):
        if self.suggestion != None:
            return "It looks like you meant to use '{}'.".format(self.suggestion)
        
        return "Looks like you used an incorrect word."


class LanguageErrorOther(LanguageError):
    """Any other type of error that is not explicitly caught."""

    def __init__(self, match):
        LanguageError.__init__(self, match)
        self.type = "other"


class LanguageErrorFactory:
    """
    This factory creates language error objects based on the type.
    The type is part of the match object, returned by the language tool API.
    """

    def create(match):
        error_type = match["rule"]["issueType"]

        if error_type == "misspelling":
            return LanguageSpellingError(match)
        elif error_type == "non-conformance":
            return LanguageNonConformanceError(match)
        elif error_type == "grammar":
            return LanguageGrammarError(match)
        else:
            # Fallback, because other type of error was detected
            return LanguageErrorOther(match)


class LanguageToolApiCheckResponse:
    """
    Wrapper for the response received from language tool API.
    For every error encountered, a simpler object is created by the factory.
    """

    def __init__(self, input_text, response):
        self.input_text = input_text
        self.response = response
        self.input_words = self._extract_words(input_text)
        self.errors = self._create_errors(response)

    def contains_error(self):
        return self.error_count() > 0

    def error_count(self):
        return len(self.errors)
    
    def error_ratio(self):
        """Ratio of errors per word."""
        word_count = len(self.input_words)
        return self.error_count() / word_count
    
    def ignore_hesitation_errors(self):
        """Removes hesitation words (uhm, eh, ehm, etc.) from the list of errors"""
        def is_hesitation(err):
            word = err.error
            word = re.sub('[\.\,\:\(\)\?\!\&]', '', word)
            word = word.lower()
            return re.search('^[haeou][hmour]+$', word) != None
        
        self.errors = list(filter(lambda err: not is_hesitation(err), self.errors))

    def ignore_entity_errors(self, nlu_entities, entity_types):
        """Removes errors from the list, if it is an entity of a specific type."""
        def is_entity(err):
            for entity in nlu_entities:
                if entity["start"] <= err.start_pos and entity["end"] >= err.end_pos:
                    if entity["entity"] in entity_types:
                        return True
            return False
        
        self.errors = list(filter(lambda err: not is_entity(err), self.errors))

    def errors_to_dict(self):
        """Creates a serializable dictionary."""
        return list(map(lambda e: e.__dict__, self.errors))
    
    def _create_errors(self, response):
        """Uses the factory to create simpler instances of language errors detected by language tool."""
        list_of_errors = []
        
        for match_index, match in enumerate(response["matches"]):
            error = LanguageErrorFactory.create(match)

            if error != None:
                list_of_errors.append(error)
        
        return list_of_errors

    def _extract_words(self, input_text):
        """Splits the input by space characters"""
        return re.split("\s+", input_text)
        

class LanguageToolApi:
    """
    A service to communicate with the language tool API.
    Certain rules are disabled by default, which consideres a more lenient correction
    for the chatting enviornment.
    """
    def __init__(self, server_url, server_port, api_version="v2", verbose=False):
        self.api_url = "http://{}:{}/{}".format(server_url, server_port, api_version)
        self.language = "en-US"

        # A set of rules that should be ignored
        self.disabled_rules = [
            "UPPERCASE_SENTENCE_START",
            "METRIC_UNITS_EN_US",
            "I_LOWERCASE",
            "PUNCTUATION_PARAGRAPH_END",
            "NOW",
        ]

        # Ensures the post parameters and response are printed
        self.verbose = verbose
    
    def check(self, input_text):
        """
        Calls the check endpoint, which is responsible for detecting errors in a given text.
        Response is wrapped in a custom response object.
        """
        url = self.api_url + "/check"

        request_parameters = {
            "text": input_text,
            "language": self.language,
            "disabledRules": ",".join(self.disabled_rules)
        }

        response = requests.post(url, data=request_parameters)

        if response.status_code != 200:
            raise ValueError(response.text)

        if self.verbose:
            print(request_parameters)
            print(response.json())

        return LanguageToolApiCheckResponse(input_text, response.json())

