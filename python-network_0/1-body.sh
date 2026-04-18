#!/bin/bash
# Sends GET request and displays response body
printf "%s" "$(curl -s "$1")"
