#!/usr/bin/env python

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
import string
from util.parse_inputs import parse_inputs



def rot(input_string, input_number):
    lc = string.ascii_lowercase.encode()
    uc = string.ascii_uppercase.encode()
    trans = bytes.maketrans(lc + uc,
        lc[input_number:] + lc[:input_number] + uc[input_number:] + uc[:input_number])
    return bytes.translate(input_string.encode(), trans)



def iter_rot(input_list):
    for list_item in input_list:
        i = 0 # iterator
        while i < 26:
            print(str(i) + str('\t') + rot(list_item, i).decode())
            i += 1 # increment iterator



if __name__ == "__main__":
    input_value = parse_inputs()
    if input_value:
        iter_rot(input_value)
    else:
        print("Provide string as argument")