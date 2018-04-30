#!/usr/bin/env bash

set -eo pipefail

# need to use python from virtual environment for commands like 'sls invoke local', 'sls deploy'...
pipenv run node_modules/serverless/bin/serverless $@
