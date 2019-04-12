
"""
0.
"""

while True:
    try:


    except (EOFError):
      break

########################################################

import os
import sys


"""
1. Complete the simpleArraySum function below.
"""
def simpleArraySum(ar):
    #
    # Write your code here.
    return sum(list(ar))

a = simpleArraySum([1,2,3,5,6])
print(a)


"""
2. Complete the compareTriplets function below.
"""

while True:
  try:
    a1, a2, a3 = input().strip().split()
    A = [int(a1), int(a2), int(a3)]
    b1, b2, b3 = input().strip().split()
    B = [int(b1), int(b2), int(b3)]
    alice = 0
    bob = 0

    for i in range(3):
        if A[i] > B[i]: alice+=1
        if A[i] < B[i]: bob+=1
        if A[i] == B[i]: continue
    print(alice, bob)

  except (EOFError):
    break

"""
3. Complete the aVeryBigSum function below.
"""

while True:
    try:
        ar = input()
        sum(map(int, ar.split()))

    except (EOFError):
      break

"""
4. Diagonal Difference
"""

n = int(input())
arr = []
for i in range(0, n):
    x = list(map(int, input().split()))
    arr.append(x)

right = 0
for i in range(0, n):
    right += arr[i][i]

left = 0
for i in range(0, n):
    left += arr[i][n-(i+1)]

print(abs(right - left))


"""
5. Complete the plusMinus function below.
"""

while True:
    try:


    except (EOFError):
      break


arr = list(map(int, input().split()))
a = arr[:-1]
b = arr[1:]
print(a, b)
