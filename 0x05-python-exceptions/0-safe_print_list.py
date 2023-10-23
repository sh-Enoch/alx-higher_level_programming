#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for item in my_list:
        if count >= x:
            break
        try:
            print(item, end=' ')
            count += 1
        except:
            pass
    print()
    return count
