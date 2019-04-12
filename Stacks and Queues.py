
import sys

chars = list('あいうえお')
chars = [bytes(char, 'utf-8') for char in chars]
sys.stdout.buffer.writelines(chars)
# あいうえお

for char in chars:
    sys.stdout.buffer.write(char)
    sys.stdout.write('\n')
    sys.stdout.flush()
# あ
# い
# う
# え
# お

while True:
  try:
    value = raw_input()
    do_stuff(value) # next line was found
  except (EOFError):
    break #end of file reached

"""
イテレータをリストの違い
1. 偶数
2. ペアになっている
3. 全てOK
関数の外で return が使用された可能性があります。(def 以外でreturn が使用された)
"""

while True:
  try:
      dict = {
      "]": "[",
      ")": "(",
      "}": "{",}
      num = int(input())
      for i in range(num):
          #Do whatever you want
          my_input = list(input())
          length = len(my_input)

          if length % 2 == 1:
              sys.stdout.write("NO")
              sys.stdout.write("\n")
              sys.stdout.flush()
              continue

          half = length // 2
          first = my_input[:half]
          second = my_input[half:]
          rev_second = list(reversed(second))
          third = []
          for e in rev_second:
              third.append(dict[e])

          if first != third:
              sys.stdout.write("NO")
              sys.stdout.write("\n")
              sys.stdout.flush()
              continue
          else:
              sys.stdout.write("YES")
              sys.stdout.write("\n")
              sys.stdout.flush()

  except (EOFError):
    break #end of file reached
