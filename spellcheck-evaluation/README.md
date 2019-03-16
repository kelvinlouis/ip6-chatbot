# Spellcheck Evaluation Scripts
All of the spellcheckers and libraries need a running unix environment.
It won't work on windows.

## Lookup table
Creates a frequency-based lookup table out of the context-sensitive words of the chatbot domain.
It is necessary for the Hunspell + Context evaluation.

### Create
In order to generate the lookup table, you need to run:
```
python create_lookup.py
```
It will use `data/all_corrected_utterances.txt` as the input and generate `context_dist.txt`
### Important
The Hunspell + Context evaluation script uses a manually modified version of the generated output.
The file is located here: `data/context_dist_small.txt`

## Spellcheckers
The following configurations of spellcheckers are evaluated
- Hunspell standalone
- Hunspell with context sensitive lookup table (using symspell)
- Symspell
- LanguageTool with language model (ngram)

### Hunspell
The hunspell directory contains all the necessary dictionary files to run.

### Symspell
The dictionary contains the frequency table which symspell uses.

## Language Tool
In order to run language tool successfully, we recommend the following steps:
- Create a folder `LanguageTool-4.4` within `spellcheckers`
- Install version 4.4 of language tool within that folder.
- Make sure you download the [n-gram language model](http://wiki.languagetool.org/finding-errors-using-n-gram-data). You can find the 8GB file [here](https://languagetool.org/download/ngram-data/ngrams-en-20150817.zip). Make sure the `LanguageTool-4.4` directory contains a `language-model` folder where the contents of the zip can be moved to.
- Make sure you configure language tool to use the language model: Create a `.languagetool.cfg` file within `LanguageTool-4.4` and append `languageModel=./language-model` to it. 
- After the installation you should be able to run the [following commands](http://wiki.languagetool.org/http-server) to start the server.
- To check if the language model is configured correctly, refer to the [following test sentences](http://wiki.languagetool.org/finding-errors-using-n-gram-data).

## Run evaluation script
In order to run the evaluation script, enter the following command:
```
python evaluate_spellcheckers
# or for debug mode
python evaluate_spellcheckers -d
```
It will print confusion matrices for every evaluated spell checker.