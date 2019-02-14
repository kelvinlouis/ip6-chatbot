const minimist = require('minimist');
const fs = require('fs');
const path = require('path');

const argv = minimist(process.argv.slice(2));
const inputPath = argv.i;
const outputPath = argv.o;

if (!inputPath) {
  throw new Error('No Input Paramter provided with flag -i path_to_file_json');
}

if (!outputPath) {
  throw new Error('No Output Paramter provided with flag -o path_to_file_json');
}

if (inputPath) {
  const output = [];
  const json = readJSON(inputPath);
  const intents = Object.keys(json);

  intents.forEach((intentName) => {
    const permutations = json[intentName];
    output.push(`## intent:${intentName}`);

    permutations.forEach((permutation) => {
      const permutationMd = [];
      permutation.forEach((block) => {
        if (block.type === 'Text') {
          permutationMd.push(block.value);
        } else if (block.type === 'Slot') {
          permutationMd.push(`[${block.value}](${block.slot})`);
        }
      });

      output.push(`- ${permutationMd.join('')}`);
    });

    output.push('');
  });

  fs.writeFile(outputPath, output.join('\n'), (err) => {
    if (err) {
      return console.log(err);
    }

    console.log("The file was saved!");
  }); 
}

function readJSON(path) {
  if (fs.existsSync(path)) {
    return JSON.parse(fs.readFileSync(path, 'utf-8'));
  }
  throw new Error('No file found');
}