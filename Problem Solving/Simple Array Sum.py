#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    x = 0
    for i in ar:
        x += i
    
    return x    #Another way, return sum(ar)

if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    print(simpleArraySum(ar))
