#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):

    if "D" not in s:
        return 0

    list = [0]
    param = 0
    for i in range(n):
        if s[i] == "D":
            param -= 1
            list.append(param)
        elif s[i] == "U":
            param += 1
            list.append(param)

    criteria = 0
    for i in range(1, len(list)):
        if list[i-1] > list[i]:
            criteria = list[i-2]
            break # continue

    counter = 1
    for i in range(1, len(list)):
        if list[i] >= criteria:
            counter += 1
            for k in range(i+1, len(list)-1):
                if list[k+1] > list[k]:
                    continue
                else:
                    criteria = list[k]
                    break

    return counter
