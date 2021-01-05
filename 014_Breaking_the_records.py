#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.
def breakingRecords(scores):
    firstscore = []
    firstscore.append(scores[0])
    firstscore2 = []
    firstscore2.append(scores[0])
    bad = 0
    good = 0
    for i in scores:
        if i < firstscore[0]:
            firstscore.append(i)
            firstscore.remove(firstscore[0])

            bad += 1
    for i in scores:
        if i > firstscore2[0]:
            firstscore2.append(i)
            firstscore2.remove(firstscore2[0])

            good += 1

    return good, bad


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
