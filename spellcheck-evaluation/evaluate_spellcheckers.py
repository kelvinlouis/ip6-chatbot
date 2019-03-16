import re
import os
import argparse
import requests
from pandas import read_csv
from nltk import word_tokenize
import hunspell
from symspellpy.symspellpy import SymSpell, Verbosity
from language_tool_api import check
from utils import proxy_debug
from normalize import remove_non_ascii, to_lowercase, remove_punctuation, remove_numbers

def create_words(row):
  """Splits the input of a row into words and removes punctuation and non_ascii character"""
  words = re.split("\s+", row["input"])
  words = remove_non_ascii(words)
  words = remove_punctuation(words)
  return words

def str_to_list(str):
  """Returns a numerical list"""
  return list(map(int, str.split(",")))

def is_hesistation_word(word):
  """Checks if word is a hesistation word (uhm, eh, ehm, etc.)"""
  return re.search('^[haeou][hmour]+$', word) != None

def create_context_speller():
  """Creates a context speller, which uses the context frequency lookup table"""

  # Initialize Context Symspell Checker
  context_sym_spell = SymSpell(83000, 2, 7)

  # load dictionary
  lookup_path = os.path.join(os.path.dirname(
      __file__), "./data/dict/context_dist_small.txt")

  if not context_sym_spell.load_dictionary(lookup_path, 0, 1):
    raise Exception("Dictionary file not found")

  # Creates the spell checker
  def check_spell(word): 
    suggestions = context_sym_spell.lookup(word, Verbosity.CLOSEST, 2)
    if len(suggestions) == 0:
      # Not in context
      return True
    else:
      correct = True
      for suggestion in suggestions:
        if suggestion.distance == 1:
          correct = False
        
      return correct
  
  return check_spell

# Add cli arguments
parser = argparse.ArgumentParser()
parser.add_argument("--debug", "-d", help="activates debug mode", action="store_true")
args = parser.parse_args()

# Creates the proxied debugger
debug = proxy_debug(args.debug)

# Tokenize the misspelled sentences
df = read_csv("./data/errors/spelling_unsanitized.csv")
df["words"] = df.apply(lambda row: create_words(row), axis=1)

# Creates the context aware spell checker
context_spelled_correct = create_context_speller()

# print(context_spelled_correct("So"))
# print(context_spelled_correct("also"))
# print(context_spelled_correct("omega"))
# print(context_spelled_correct("switch"))
# print(context_spelled_correct("equipped"))
# print(context_spelled_correct("able"))
# print(context_spelled_correct("list"))
# print(context_spelled_correct("witch"))

# raise Error("TEST")

language_tool_check = lambda text: check(text, "http://localhost:8081/v2/", "en-US", disabled_rules="UPPERCASE_SENTENCE_START,METRIC_UNITS_EN_US,I_LOWERCASE")

# ##########################
# # Evaluate Hunspell
# ##########################
hs = hunspell.HunSpell("./spellcheckers/hunspell/en_US.dic", "./spellcheckers/hunspell/en_US.aff")
# # hs = hunspell.HunSpell("./spellcheckers/hunspell/en_GB.dic", "./spellcheckers/hunspell/en_GB.aff")
# TP, FP, FN, TN
hs_cm = [0, 0, 0 , 0]

for row_index, row in df.iterrows():
  expected_errors = str_to_list(row["error_pos"])

  for word_index, word in enumerate(row["words"]):
    if re.search('\d', word):
      # Ignore if word contains a number => correct word
      hs_cm[3] = hs_cm[3] + 1
      continue

    # Hunspell is a case-sensitive checker, thus check all possible cases
    word_lower = word.lower()
    word_upper = word.upper()
    word_pascal = word.title()
    misspelled = (hs.spell(word) == False) and (hs.spell(word_lower) == False) and (hs.spell(word_pascal) == False) and (hs.spell(word_upper) == False)

    if misspelled == True:
      # Ignores hesistation word
      misspelled = is_hesistation_word(word_lower) == False

    if misspelled == True:
      if word_index in expected_errors:
        # TP
        hs_cm[0] = hs_cm[0] + 1
      else:
        # FP
        debug("Hunspell False/Positive: " + word)
        hs_cm[1] = hs_cm[1] + 1
    else:
      if word_index in expected_errors:
        # FN
        debug("Hunspell False/Negative: " + word)
        hs_cm[2] = hs_cm[2] + 1
      else:
        # TN
        hs_cm[3] = hs_cm[3] + 1

debug("Hunspell Confusion Matrix: (TP, FP, FN, TN)" + str(hs_cm))

# ##########################
# # Evaluate Hunspell + Context
# ##########################
# TP, FP, FN, TN
hs_ctx_cm = [0, 0, 0, 0]

for row_index, row in df.iterrows():
  expected_errors = str_to_list(row["error_pos"])

  for word_index, word in enumerate(row["words"]):
    if re.search('\d', word):
      # Ignore if word contains a number => correct word
      hs_ctx_cm[3] = hs_ctx_cm[3] + 1
      continue

    # Hunspell is a case-sensitive checker, thus check all possible cases
    word_lower = word.lower()
    word_upper = word.upper()
    word_pascal = word.title()
    misspelled = (hs.spell(word) == False) and (hs.spell(word_lower) == False) and (
        hs.spell(word_pascal) == False) and (hs.spell(word_upper) == False)
    
    if misspelled == True and is_hesistation_word(word_lower) == True:
      # Ignores hesistation word
      hs_ctx_cm[3] = hs_ctx_cm[3] + 1
      continue

    ctx_spelling_correct = context_spelled_correct(word_lower)

    if misspelled == True or ctx_spelling_correct == False:
      if word_index in expected_errors:
        # TP
        hs_ctx_cm[0] = hs_ctx_cm[0] + 1
      else:
        # FP
        debug("Hunspell + Context False/Positive: " + word)
        hs_ctx_cm[1] = hs_ctx_cm[1] + 1
    else:
      if word_index in expected_errors:
        # FN
        debug("Hunspell + Context False/Negative: " + word)
        hs_ctx_cm[2] = hs_ctx_cm[2] + 1
      else:
        # TN
        hs_ctx_cm[3] = hs_ctx_cm[3] + 1

debug("Hunspell + Context Confusion Matrix: (TP, FP, FN, TN)" + str(hs_ctx_cm))


# ##########################
# # Evaluate Symspell
# ##########################
ss_cm = [0, 0, 0, 0]
initial_capacity = 83000
max_edit_distance_dictionary = 2
prefix_length = 7
sym_spell = SymSpell(initial_capacity, max_edit_distance_dictionary, prefix_length)

# load dictionary
dictionary_path = os.path.join(os.path.dirname(__file__), "./spellcheckers/symspell/frequency_dictionary_en_82_765.txt")

term_index = 0  # column of the term in the dictionary text file
count_index = 1  # column of the term frequency in the dictionary text file

# max edit distance per lookup
# (max_edit_distance_lookup <= max_edit_distance_dictionary)
max_edit_distance_lookup = 2
suggestion_verbosity = Verbosity.CLOSEST  # TOP, CLOSEST, ALL

if not sym_spell.load_dictionary(dictionary_path, term_index, count_index):
  raise Exception("Dictionary file not found")

for row_index, row in df.iterrows():
  expected_errors = str_to_list(row["error_pos"])

  for word_index, word in enumerate(row["words"]):
    if re.search('\d', word):
      # Ignore if word contains a number => correct word
      ss_cm[3] = ss_cm[3] + 1
      continue

    suggestions = sym_spell.lookup(word.lower(), suggestion_verbosity, max_edit_distance_lookup)
    spelling_correct = False
    for suggestion in suggestions:
      if (suggestion.distance == 0):
        spelling_correct = True

    if spelling_correct == False:
      # Ignore hesitation words
      spelling_correct = is_hesistation_word(word_lower)

    if spelling_correct == False:
      if word_index in expected_errors:
        # TP
        ss_cm[0] = ss_cm[0] + 1
      else:
        # FP
        debug("Symspell False/Positive: " + word)
        ss_cm[1] = ss_cm[1] + 1
    else:
      if word_index in expected_errors:
        # FN
        debug("Symspell False/Negative: " + word)
        ss_cm[2] = ss_cm[2] + 1
      else:
        # TN
        ss_cm[3] = ss_cm[3] + 1

debug("Symspell Confusion Matrix: (TP, FP, FN, TN)" + str(ss_cm))


##########################
# Evaluate LanguageTool (n-gram)
##########################
lt_ngram_cm = [0, 0, 0, 0]

for row_index, row in df.iterrows():
  sentence = row["input"]
  all_words = row["words"]
  all_predicted_error_pos = []
  all_expected_error_pos = str_to_list(row["error_pos"])
 
  response = language_tool_check(sentence)

  for match_index, match in enumerate(response["matches"]):
    error_type = match["rule"]["issueType"]
    error_start = match["offset"]
    error_len = match["length"]

    # Extracts the word where the error occurred
    error_word = sentence[error_start:error_start+error_len]

    # Count number of words before the error
    words_before = re.split("\s+", sentence[:error_start])

    # Calculate word position of error
    predicted_error_pos = len(words_before) - 1

    if re.search('\d', error_word):
      # Ignore if word contains a number => correct word
      continue
    
    # Ignore spacing
    is_case_error = False
    error_word_lower = error_word.lower()
    error_word_pascal = error_word.title()

    if is_hesistation_word(error_word_lower) == True:
      # Ignore hesistation word
      continue

    for replacement in match["replacements"]:
      value = replacement["value"].lower()

      if value == error_word_lower or value == error_word_pascal:
        is_case_error = True
        break
    
    if is_case_error == True:
      # debug("Case error found ({}): Suggestion {}".format(error_word, value))
      continue
    
    if error_type != "misspelling":
      # Check if differently classified compared to our definitions
      if predicted_error_pos not in all_expected_error_pos:
        debug("Different error found ({}): {}".format(error_type, error_word))
        continue
    
    # debug("Error pos: {} {}".format(error_start, error_len))
    # debug("Words before: {}".format(words_before))
    # debug("Is in error? {} -> {}".format(predicted_error_pos, all_expected_error_pos))
    
    # Add to list of predicted errors
    all_predicted_error_pos.append(predicted_error_pos)

  for word_index, word in enumerate(all_words):
    is_predicted_error = word_index in all_predicted_error_pos
    is_expected_error = word_index in all_expected_error_pos

    if is_predicted_error == True and is_expected_error == True:
      # TP
      lt_ngram_cm[0] = lt_ngram_cm[0] + 1
    elif is_predicted_error == True and is_expected_error == False:
      # FP
      debug("LanguageTool (ngram) False/Positive: " + word)
      lt_ngram_cm[1] = lt_ngram_cm[1] + 1
    elif is_predicted_error == False and is_expected_error == True:
      # FN
      debug("LanguageTool (ngram) False/Negative: " + word)
      lt_ngram_cm[2] = lt_ngram_cm[2] + 1
    else:
      # TN
      lt_ngram_cm[3] = lt_ngram_cm[3] + 1

debug("Language Tool (ngram) Confusion Matrix: (TP, FP, FN, TN)" + str(lt_ngram_cm))
