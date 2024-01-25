#!/bin/bash
#Sends a request to a urlpassed as an argument.
curl -s -o /dev/null -w "%{http_code}" "$1"
