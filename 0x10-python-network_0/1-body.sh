#!/bin/bash
# This script takes in a URL, sends a GET request, and displays the body of the response (only for 200 status code)

# Send a GET request to the specified URL, discard progress info (-s), and display the body for a 200 status code
curl -s -o /dev/null -w "%{http_code}" "$1" | {
    read -r status_code
    if [ "$status_code" -eq 200 ]; then
        curl -s "$1"
    fi
}
