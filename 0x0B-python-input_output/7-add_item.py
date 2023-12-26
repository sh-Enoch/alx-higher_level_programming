#!/usr/bin/python3
"""Adds all arguments to apython list and save them."""
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

content = argument passed
with open("holder.txt","a") as file:
    file.write(content)


