#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) != 0:
        new_list = list(reversed(my_list))
        for i in new_list:
            print("{:d}".format(i))
