#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return my_list
    reversed = my_list[::-1]
    for i in reversed:
        print("{:d}".format(i))
