#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    x = 0
    y = 0
    z = 0

    for i in range(0, len(arr)):
        if arr[i] < 0:
            x += 1 / n
        elif arr[i] == 0:
            y += 1 / n
        elif arr[i] > 0:
            z += 1 / n

    print(z)
    print(x)
    print(y)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
