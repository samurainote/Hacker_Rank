import math
import os
import random
import re
import sys
import numpy as np


# Complete the rotLeft function below.
def rotLeft(a, d):
    # d = num of rotation
    # a = array
    nums = np.array(a)
    lnums = nums.tolist()
    length = len(list(a))
    if d < length:
        sub = nums[:d+1]
        ans = nums[d+1:]
        ans = ans + sub
        return ans

    if d = length:
        return nums

    if d > length:
        rest = d % length
        sub = nums[:rest+1]
        ans = nums[rest+1:]
        ans = ans + sub
        return ans
