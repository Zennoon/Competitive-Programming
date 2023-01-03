#!/bin/python3

import math
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    num = arr[len(arr) - 1]
    for i in range(2, len(arr) + 1):
        ind = len(arr) - i
        if (arr[ind] > num):
            arr[ind + 1] = arr[ind]
            print(" ".join(str(num) for num in arr))
        else:
            arr[ind + 1] = num
            break
    if arr[0] > num:
        arr[0] = num
    print(" ".join(str(num) for num in arr))

