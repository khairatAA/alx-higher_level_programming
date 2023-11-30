#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -s -X "POST" $2 -o dev/null $1
