#!/usr/bin/env bash

# Generate the static site

pushd client

npm run-script build

popd