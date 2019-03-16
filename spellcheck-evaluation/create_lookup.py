from nltk import word_tokenize, FreqDist
from normalize import normalize

# Normalize text
file_unsanitized = open("./data/dict/all_corrected_utterances.txt")
raw_unsanitized = file_unsanitized.read()
tokens_unsanitized = word_tokenize(raw_unsanitized)
tokens_normalized = normalize(tokens_unsanitized)

# Calculate word/token distribution
dist = FreqDist(tokens_normalized)

file_frequency_dist = open("./data/dict/context_dist.txt", "w")

for word_dist in dist.most_common():
  file_frequency_dist.write(word_dist[0] + " " + str(word_dist[1]))
  file_frequency_dist.write("\n")

file_frequency_dist.close()
