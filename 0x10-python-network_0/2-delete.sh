#!/bin/bash
# This script sends a DELETE request to the URL and displays the body of the response

# Send a DELETE request to the specified URL, discard progress info (-s), and display the body
curl -sX DELETE "$1"
