#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -i -s -X OPTIONS $1
