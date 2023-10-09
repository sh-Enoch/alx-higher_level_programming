#!/usr/bin/python3
def no_c(my_string):
    letter_to_remove = "C"
    letter = "c"
    new =''.join(char for char in my_string if char != letter_to_remove and char != letter)
    return new
