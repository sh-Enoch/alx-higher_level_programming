#!/usr/bin/python3
def uppercase(str):
    result = ''
    for i in str:
        val = ord(i)
        if val >= 97 and val <= 122:
            val -= 32
        result += chr(val)
    print("{}\n".format(result), end="")
