#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    new = []
    try:
    count = 0
    for i in my_list:
        if type(i) == int:
            if count <= x:
                print("{}".format(i), end="")
                count = count + 1
    except IndexError as e:
        print("{}".format(e))
    return count
