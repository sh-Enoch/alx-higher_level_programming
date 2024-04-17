#!/usr/bin/python3
"""Pascal Triangle."""


def pascal_triangle(n):
    """Return a list of lists of integers of the Pascal's triangle."""
    if n <= 0:
        return []
    else:
        ls = []
        ls.append([1])

        for i in range(1, n):
            previous_row = ls[i - 1]
            current_row = [1]

            for j in range(1, i):
                current_row.append(previous_row[j - 1] + previous_row[j])
            current_row.append(1)

            ls.append(current_row)
        return ls
