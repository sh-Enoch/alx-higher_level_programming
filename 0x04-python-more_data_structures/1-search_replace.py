#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    idx = new.index(search)
    new[idx] = replace
    return new
