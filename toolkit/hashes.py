#!/usr/bin/env python


# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from sys import argv
import hashlib
from util.parse_inputs import parse_inputs
import os.path



def get_hashes(input_value):
    for i in input_value:
        if os.path.isfile(i):
            with open(i,'rb') as open_file: # rb = read/binary mode
                in_val = open_file.read()
        else:
            in_val = i.encode()
        print('Source:\t' + repr(str(i)))
        print('MD5:\t' + str(hashlib.md5(in_val).hexdigest()))
        print('SHA1:\t' + str(hashlib.sha1(in_val).hexdigest()))
        print('SHA224:\t' + str(hashlib.sha224(in_val).hexdigest()))
        print('SHA256:\t' + str(hashlib.sha256(in_val).hexdigest()))
        print('SHA384:\t' + str(hashlib.sha384(in_val).hexdigest()))
        print('SHA512:\t' + str(hashlib.sha512(in_val).hexdigest()))



if __name__ == "__main__":
    input_value = parse_inputs()
    if input_value:
        get_hashes(input_value)
