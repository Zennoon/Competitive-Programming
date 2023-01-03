#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    for grade in grades:
        if (grade < 38 or (not grade % 5)):
            continue
        else:
            for num in range(grade, grade + 3):
                if (not num % 5):
                    grades[grades.index(grade)] = num
    return grades


