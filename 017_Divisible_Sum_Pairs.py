#!/bin/python3

import math
import os
import random
import re
import sys
import itertools



def divisibleSumPairs(n, k, ar):
    xs = [sum(x) % k for x in itertools.combinations(ar, 2)]
    return xs.count(0)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
