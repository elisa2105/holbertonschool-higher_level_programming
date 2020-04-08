#!/bin/bash
# HTTP methods allowed
curl -sI $1 | grep "Allow" | cut -c 8-
