#!/usr/bin/bash
#display size of body response
curl "$1" | grep -i Content-Length | cut -d " " -f2
