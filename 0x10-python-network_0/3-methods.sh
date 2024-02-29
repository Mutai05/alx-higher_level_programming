#!/bin/bash
# This script takes in a URL and displays all HTTP methods the server will accept

# Send an OPTIONS request to the specified URL, discard progress info (-s), and display allowed methods
curl -sI "$1" | grep -i Allow | cut -d ' ' -f2-
