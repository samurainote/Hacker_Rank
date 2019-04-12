

"""
Reverse Integer

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21
"""

import sys

nums = str(input())
if len(nums) == 3:
    if "0" in nums:
        nums -= "0"
        if "0" in nums:
            nums -= "0"
    ans = list(reversed(nums))
    # print("".join(ans))
    sys.stdout.write("".join(ans))
elif len(nums) == 4:
    head = nums.pop(0)
    if "0" in nums:
        nums -= "0"
        if "0" in nums:
            nums -= "0"
    ans = list(head + reversed(nums))
    sys.stdout.write("".join(ans))
