#!/bin/python3

import math
import os
import random
import re
import sys

def gradingStudents(grades):
    x = []

    for i in grades:
        if i <= 35:
            x.append(i)
        elif i > 35 and i % 5 == 0:
            x.append(i)
        elif i > 35 and i % 5 != 0:
            y = 5 - (i % 5)
            if y > 2:
                z = i
                x.append(z)
            elif y <= 2:
                z = i + y
                x.append(z)

        else:
            pass

    return x


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()