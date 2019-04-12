#!/usr/bin/env python
# file_modified.py
# takes input file or string and returns file modified date

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from util.parse_inputs import parse_inputs
import os.path
import time


# -----------------------------------------------------------------------------
# Variables
# -----------------------------------------------------------------------------
time_format = "%a, %d %b %Y %H:%M:%S"


# -----------------------------------------------------------------------------
# Input should be a list of files or directories
# -----------------------------------------------------------------------------
def file_modified(input_value):
    for i in input_value:
        if os.path.exists(i):
            unix_time = os.path.getmtime(i)
            formatted_time = time.strftime(time_format, time.localtime(unix_time))

            print(str(i) + '\t' + formatted_time)
        else:
            print('Unable to find ' + str(i))



if __name__ == "__main__":
    input_value = parse_inputs(strip_newline_stdin=True)
    if input_value:
        file_modified(input_value)
