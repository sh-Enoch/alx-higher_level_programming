#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    ls = []
    for i in matrix:
        a = list(map(lambda x: x ** 2, i))
        ls.append(a)
    return ls
