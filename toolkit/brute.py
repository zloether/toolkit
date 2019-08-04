#!/usr/bin/env python

import itertools
import string
import time
from datetime import datetime


answer = 'b*0RaZ7'




def brute(max_length=14, lower=True, upper=True, digits=True, special=True, custom='', timer=True):
    char_set = __get_char_set(lower, upper, digits, special, custom)

    #start_time = time.time()
    start_time = datetime.now()
    
    counter = 0
    for password_length in range(1, max_length + 1):
        for guess in itertools.product(char_set, repeat=password_length):
            counter += 1
            password = ''.join(guess)
            
            if password == answer:
                #end_time = time.time()
                end_time = datetime.now()
                time_elapsed = end_time - start_time
                print('Password: ' + password)
                print('Attempts: ' + str(counter))
                print('Time elapsed: ' + str(time_elapsed))
                exit()
    
    print('Answer not found')



def __get_char_set(lower, upper, digits, special, custom):
    charset = ''

    if lower:
        charset = charset + string.ascii_lowercase
    
    if upper:
        charset = charset + string.ascii_uppercase
    
    if digits:
        charset = charset + string.digits
    
    if special:
        charset = charset + string.punctuation
    
    if custom:
        charset = charset + str(custom)
    
    return charset



if __name__ == '__main__':
    brute(max_length=8, lower=True, upper=True, digits=True, special=True)