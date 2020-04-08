#!/bin/bash
# curl send request body size
curl -sI "$1" | grep "Content-Length" | cut -d: -f2 | tr -d " "
