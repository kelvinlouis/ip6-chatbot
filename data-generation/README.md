# Data Generation
This directory contains all necessary scripts and dependencies to generate
intents using Chatito DSL. Chatito creates intents for the Rasa NLU using its JSON format.
We created a simple script `create-md.js` which translates the JSON into a more readable and compatible markdown file.
The markdown format is the preferred format for intents in Rasa.

## Commands

Make sure to install all dependencies.
```
npm install
```

The following command will create a JSON for every `*.chatito` file in the `chatito` directory.
```
npx chatito chatito --outputPath=out/
```

The following command uses the generated JSON and translates it to a markdown file.
```
node create-md.js -i out/default_dataset_training.json -o out_md/intents.md
```