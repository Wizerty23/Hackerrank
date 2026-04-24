#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    x, y, z = 0, 0, 0
    for i in arr:
        if i == 0:
            x += 1
        if i > 0:
            y += 1
        if i < 0:
            z += 1
    zeros = round(float(x / len(arr)), 6)
    pos = round(float(y / len(arr)), 6)
    neg = round(float(z / len(arr)), 6)

    print(pos, neg, zeros, sep="\n")

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
