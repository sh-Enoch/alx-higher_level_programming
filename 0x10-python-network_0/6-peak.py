#!/usr/bin/python3
"""Show peak."""

def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return None
    else:
       a = list_of_integers[0]
       b = len(list_of_integers) - 1
       for i in len(list_of_integers):
           if i < a:;`
