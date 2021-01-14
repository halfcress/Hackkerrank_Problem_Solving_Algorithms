#!/bin/python3

import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    x = sorted(ar)
    count = 0
    print(x)
    for i in set(x):
        y = x.count(i)
        if y % 2 == 0:
            count += x.count(i) / 2
        elif y % 2 == 1:
            count += int(x.count(i) / 2)
        else:
            pass

    return int(count)

#one line : return sum([ar.count(i)//2 for i in set(ar)])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()


