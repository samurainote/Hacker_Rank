

"""
手順
1. input
2. 単語に分割



"""

sentences = list(input().split("\n"))

total = 0
for i in len(sentences):
    words = list(map(str, input().strip().split()))
    capital = []
    number = []
    for word in words:
        if word[0].isdigit():
            number.append(word)
        elif word[0].isupper():
            capital.append(word)

    answer = len(capital) + len(number)
    total += answer

print(total)



sequences = list(map(int, input().split(",")))

for i in range(len(sequences)):
    # 奇数番目
    if i%2 != 0:
        # 一つ前の数字と違う
        if sequences[i] != sequences[i-1]:
            sequences.pop(i)

print(sequences)



while True:
  try:
      sequences = list(map(int, input().split(",")))

      for i in range(len(sequences)):
          # 奇数番目
          if i%2 != 0:
              # 一つ前の数字と違う
              if sequences[i] != sequences[i-1]:
                  sequences.pop(i)

      print(sequences)

  except (EOFError):
    break #end of file reached



# def header_reader():
from sys import stdin
lines = stdin.read().splitlines()
length = 0
sequences = []
for i in range(len(lines)):
    if i == 0:
        headers = list(map(str, input().split()))
        length = len(headers)
    else:
        sequence = list(map(int, input().split()))
        sequences.append(sequence)

sequencesT = [*zip(*sequences)]

averages = []
for tup in sequencesT:
    average = sum(list(tup)) / len(list(tup))
    averages.append(average)

# 出力
length_ave = len(averages)
if length_ave == length:
    for header in headers:
        print(header, end=",")
    for average in averages:
        print(average, end=",")
else:
    print("error")


from sys import stdin
while True:
  try:
      lines = stdin.read().splitlines()
      length = 0
      sequences = []
      for i in range(len(lines)):
          if i == 0:
              headers = list(map(str, input().split()))
              length = len(headers)
          else:
              sequence = list(map(int, input().split()))
              sequences.append(sequence)

      sequencesT = [*zip(*sequences)]

      averages = []
      for tup in sequencesT:
          average = sum(list(tup)) / len(list(tup))
          averages.append(average)

      # 出力
      length_ave = len(averages)
      if length_ave == length:
          for header in headers:
              print(header, end=",")
          for average in averages:
              print(average, end=",")
      else:
          print("error")

  except (EOFError):
    break #end of file reached
