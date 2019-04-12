#!/usr/bin/env python

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
import base64
import os.path
from util.parse_inputs import parse_inputs



def base64_decode(input_value):
    for i in input_value:
        if os.path.isfile(i): # open files
            with open(i,'rb') as open_file: # rb = read/binary mode
                in_val = open_file.read()
        elif os.path.isdir(i): # skip directories
            continue
        else: # strings
            in_val = i.encode()
        print(str(base64.b64decode(in_val).decode()))



if __name__ == "__main__":
    input_value = parse_inputs(strip_newline_stdin=True)
    if input_value:
        base64_decode(input_value)
