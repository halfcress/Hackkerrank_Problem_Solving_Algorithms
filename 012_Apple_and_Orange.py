#!/bin/python3

import math
import os
import random
import re
import sys


def countApplesAndOranges(s, t, a, b, apples, oranges):
    # STUPID POORLY WORDED QUESTION
    applecount = 0
    orangecount = 0

    for i in apples:
        if (i + a) >= s and (i + a) <= t:
            applecount += 1
    for i in oranges:
        if (i + b) >= s and (i + b) <= t:
            orangecount += 1

    print(applecount)
    print(orangecount)


# print(sum([1 for x in apple if (x + a) >= s and (x + a) <= t]))
# print(sum([1 for x in orange if (x + b) >= s and (x + b) <= t]))


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
