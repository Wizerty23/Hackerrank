#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    a = ""
    for c in sentence:
        if c.isupper() == True:
            a += c.lower()
        else:
            a += c.upper()
        
    b = a.split() #Here the cases are swapped
    c = []
    for i in range(len(b)):
        c.append(b[len(b)-i-1])
        
    x = " ".join(c)

    return x  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()