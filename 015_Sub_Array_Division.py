#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the birthday function below.
def birthday(s, d, m):
    # liste1 = [] #[[1, 2], [2, 1], [1, 3], [3, 2]]
    # liste2 = []
    count = 0

    for i in range(0, (len(s) + 1 - m)):
        if sum(s[i:i + m]) == d:
            count += 1
    #    liste1.append(s[i:(m+i)])
    # for i in range(len(s)-m+1):
    #    if sum(liste1[i:i+m]) == d:
    #        count += 1

    return count
    # tp = (len(s)-m) + 1 #total number of pieces possible
    # return len([1 for i in range(tp) if sum(s[i:i+m])==d])
    #tek satır versiyon;
    # return len([1 for i in range((len(s)-m) + 1) if sum(s[i:i+m])==d])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
