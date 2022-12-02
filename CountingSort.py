#!/bin/python3

import math
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    frequencyArr = []
    for ind in range(100):
        frequencyArr.append(0)
    for num in arr:
        frequencyArr[num] += 1
    return frequencyArr
