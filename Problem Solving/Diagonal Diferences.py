#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    columns = len(arr[0])
    x, y, a, b = 0, 0, 0, 0
    for _ in range(columns):
        a += arr[x][y]
        b += arr[x][columns-y-1] #You have to add -1 because the counting starts at 0
        x += 1
        y += 1
        #print(a,b)
    
    return abs(a-b)

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    print(diagonalDifference(arr))
