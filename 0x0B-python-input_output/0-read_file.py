#!/usr/bin/python3
def read_file(filename=""):
    """ reads a text file"""

    with open(filename, 'r', encoding="utf-8") as file:
        data = file.read()
        print(data)
