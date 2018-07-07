#!/usr/bin/env bash

echo "$GIST_PERSONAL_TOKEN" > ~/.gist
gist "$@"
