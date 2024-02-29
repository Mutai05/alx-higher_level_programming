#!/bin/bash
# This script takes in a URL, sends a request, and displays the size of the body in bytes

# Send a GET request to the specified URL, discard progress info (-s), and display the size of the body
curl -sI "$1" | grep -i Content-Length | awk '{print $2}' 
