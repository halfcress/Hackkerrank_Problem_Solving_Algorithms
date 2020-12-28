#!/bin/python3

import math
import os
import random
import re
import sys

# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    primal = list()
    second = list()
    sumpri = 0
    sumsec = 0

    for i in range(0, len(arr)):
        x = arr[i][i]
        primal.append(x)
    for i in range(0, len(arr)):
        y = arr[i][-(i + 1)]
        second.append(y)

    for i in primal:
        sumpri += i
    for i in second:
        sumsec += i

    absolute = abs(sumpri - (sumsec))

    return absolute


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
