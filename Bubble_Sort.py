#!/bin/python3

import math
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    swaps = 0
    sorted_a = sorted(a)
    while a != sorted_a:
        for ind in range(len(a) - 1):
            if a[ind] > a[ind + 1]:
                temp = a[ind]
                a[ind] = a[ind + 1]
                a[ind + 1] = temp
                swaps += 1
    print("Array is sorted in", swaps, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[len(a) - 1])
    return


