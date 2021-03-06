### Train NLU
`python -m rasa_nlu.train -c config_nlu.yml -d data/nlu -o models/nlu --fixed_model_name test --project default`

### Interactive learning with training
`python -m rasa_core.train interactive -o models/dialogue -d domain.yml -c config_core.yml -s data/stories -u models/nlu/default/test --endpoints endpoints.yml`

### Interactive learning without training
`python -m rasa_core.train interactive -o models/dialogue -d domain.yml -c config_core.yml --core models/dialogue -u models/nlu/default/test --endpoints endpoints.yml`

### Train Core without interactive learning
`python -m rasa_core.train default -o models/dialogue -d domain.yml -c config_core.yml -s data/stories`

### Run Action Server
`python -m rasa_core_sdk.endpoint --actions actions`

### Run Core Server
`python -m rasa_core.run -d models/dialogue --endpoints endpoints.yml --port 5002 --credentials credentials.yml -o logs/core.log --enable_api -u default/test -v`

### Run NLU Server
`python -m rasa_nlu.server --path models/nlu --response_log logs/response.log -w logs/nlu.log -P 5000`

### Run NLU + Core together: Endpoint: ws://localhost:5002/socket.io/
`python -m rasa_core.run -d models/dialogue -u models/nlu/default/test --endpoints endpoints.yml --port 5002 --credentials credentials.yml -o logs/core.log`

### Evaluate NLU
`python -m rasa_nlu.evaluate --data data/test_nlu --model models/nlu/default/test --errors eval_results/nlu/test_errors.json --histogram eval_results/nlu/test_histogram --confmat eval_results/nlu/test_confmat`

### Evaluate Core
`python -m rasa_core.evaluate --core models/dialogue --stories test_stories.md -o results`

### Evaluate with NLU (Bug: https://github.com/RasaHQ/rasa_core/issues/1394)
`python -m rasa_core.evaluate default --core models/dialogue --nlu models/nlu/default/test --stories data/e2e_stories --e2e`

### Evaluate different Policies
`python -m rasa_core.train compare -c config_core.yml config_core_redp.zml -d domain.yml -s stories_folder -o comparison_models --runs 3 --percentages 0 5 25 50 70 90 95`
