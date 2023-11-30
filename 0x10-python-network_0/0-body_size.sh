#!/bin/bash
# cURL body size

curl -s -o /dev/null -w "%{size_download}\n" "$1"
