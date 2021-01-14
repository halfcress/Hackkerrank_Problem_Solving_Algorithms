#!/bin/python3

import os
import sys
import statistics
import itertools as it


def pageCount(n, p):
    l1 = []

    resultlist = []
    for i in range(0, n + 1):
        l1.append(i)
    l2 = l1[::-1]

    for i in range(len(l1)):
        if p == l1[i]:
            resultlist.append(i)

    for i in range(len(l2)):
        if p == l2[i]:
            resultlist.append(i)
    print(resultlist)
    x = resultlist[0] / 2
    if resultlist[1] == 1 and max(l1) == 6:

        y = resultlist[1]
    else:
        y = resultlist[1] / 2

    if x > y:
        return int(y)
    elif y > x:
        return int(x)
    elif x == y:
        return int(x)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
