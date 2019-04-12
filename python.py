

sys.stdout.write("YES")
sys.stdout.write("\n")
sys.stdout.flush()

while True:
  try:

  except (EOFError):
    break #end of file reached

from collections import deque

#########################################################################################################

while True:
  try:
      lens = list(map(int, input().split()))
      tower0 = list(map(int, input().split()))
      tower1 = list(map(int, input().split()))
      tower2 = list(map(int, input().split()))

      rs0 = tower0[::-1]
      rs1 = tower1[::-1]
      rs2 = tower2[::-1]

      # 基準を決める
      for _ in range(max(lens)):
        if sum(rs0) == sum(rs1) and sum(rs1) == sum(rs2):
          sys.stdout.write(str(sum(rs0)))
          sys.stdout.flush()
          break
        else:
          mini = min([sum(rs0), sum(rs1), sum(rs2)])
          while sum(rs0) > mini:
            rs0.pop()
          while sum(rs1) > mini:
            rs1.pop()
          while sum(rs2) > mini:
            rs2.pop()

  except (EOFError):
    break #end of file reached
