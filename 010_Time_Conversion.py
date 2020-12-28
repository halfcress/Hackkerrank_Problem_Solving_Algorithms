#!/bin/python3

import os
import sys

def timeConversion(s):
    dilim = (10 * int(s[0])) + (int(s[1]))
    dilim2 = 12 + dilim

    if s[0] == "1" and s[1] == "2" and s[8] == "A":
        return "00" + str(s[2:8])
    elif s[0] == "1" and s[1] == "2" and s[8] == "P":
        return s[0:8]

    elif s[8] == "A":
        return s[0:8]

    elif s[8] == "P":

        return str(dilim2) + str(s[2:8])


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
