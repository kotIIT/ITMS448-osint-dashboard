#!/usr/bin/env bash

pushd bowser/

python3 -m pipenv run python3 bowserHTTPAPI.py

popd