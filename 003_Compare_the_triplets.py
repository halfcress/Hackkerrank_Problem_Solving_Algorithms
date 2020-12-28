#!/bin/python3

import math
import os
import random
import re
import sys


def compareTriplets(a, b):
    a_score = 0
    b_score = 0

    for i in range(0, 3):
        if a[i] > b[i]:
            a_score += 1
        elif a[i] == b[i]:
            pass
        elif b[i] > a[i]:
            b_score += 1

    result = [a_score, b_score]
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
