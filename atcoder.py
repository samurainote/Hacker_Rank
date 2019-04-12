"""
入力: 入力は以下の形式で標準入力から与えられる。
a b
出力: 積が奇数なら Odd と、 偶数なら Even と出力せよ。
Even
"""

# Q.1
import sys

nums = list(map(int, input().split()))
start = 1
for e in nums:
    start * e

if start % 2 == 1:
    sys.stdout.write("Odd")
    sys.stdout.write("\n")
    sys.stdout.flush()
else:
    sys.stdout.write("Even")
    sys.stdout.write("\n")
    sys.stdout.flush()

"""
3つ
"""
# Q.2

lists = list(map(int, input().split()))
counter = 0
for n in lists:
    if n == 0:
        continue
    elif n == 1:
        counter += 1

sys.stdout.write(str(counter))
sys.stdout.write("\n")
sys.stdout.flush()
