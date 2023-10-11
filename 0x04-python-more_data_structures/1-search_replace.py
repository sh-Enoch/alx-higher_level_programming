#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for i in new:
        if i == search:
            a = new.index(i)
            new[a] = replace
    return new
