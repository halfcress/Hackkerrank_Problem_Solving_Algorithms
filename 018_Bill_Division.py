#!/bin/python3

import math
import os
import random
import re
import sys


def bonAppetit(bill, k, b):
    bill.remove(bill[k])
    y = sum(bill) / 2
    if b > y:
        x = b - y
        x = int(x)
        print(x)


    else:
        print("Bon Appetit")


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
