#!/bin/python3

import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    sorted(arr)
    x = 0
    y = 0

    for i in arr:
        x += i

    for i in arr:
        y += i

    maximum = x - min(arr)
    minimum = x - max(arr)

    print(minimum, maximum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
