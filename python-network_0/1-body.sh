#!/bin/bash
# Sends GET request and displays body only if response code is 200
resp=$(curl -s -w "%{http_code}" "$1"); code=${resp: -3}; [ "$code" -eq 200 ] && echo "${resp%???}"
