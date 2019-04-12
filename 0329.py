
"""
２匹の猫のどっちが先に捕まえるか
同時に到着するとネズミにげる
Complete the catAndMouse function below.
"""
# 3 input
# catA = int(input())
n = int(input())
for i in range(n):
    line = list(map(int, input().strip().split()))
    x, y, z = line[0], line[1], line[2]
    A = abs(x-z)
    B = abs(y-z)

    if A < B:
        print("Cat A")
    elif A > B:
        print("Cat B")
    else:
        print("Mouse C")


"""
3*3 matrixの差分をコストに
Complete the formingMagicSquare function below.
# 3line input
# 1int output
"""

def formingMagicSquare():
    # default
    matrixA = []
    for i in range(3):
        line = list(map(int, input().split()))
        matrixA.append(line)

    matrixB = []
    for i in range(3):
        line = list(map(int, input().split()))
        matrixB.append(line)

    total = 0
    for i in range(3):
        for k in range(3):
        cost = abs(matrixA[i][k]-matrixB[i][k])
        total += cost

    matrixA = matrixB

    return total

"""
3*3 matrixの差分をコストに
Complete the formingMagicSquare function below.
# 3line input
# 1int output

手順がある
1. 3行の読み込み
2. 1~9で足りない数字を読みこむ
3. 重複している数字を洗い出す
4. 条件：ミニマムコストで
"""

def read_square():
    matrixA = []
    for i in range(3):
        line = list(map(int, input().split()))
        matrixA.append(line)
    return matrixA

def base_creater():
    base = []
    for i in range(1,10):
        base.append(i)
    return base

def gap_founder(matrix, base):
    uniques = []
    for i in range(3):
        for k in range(3):
            uniques.append(matrix[i][k])
    checker = []
    duplicates = []
    for e in uniques:
        if e in checker:
            duplicates.append(e)
        else:
            checker.append(e)
    lacks = base-set(uniques)
    return lacks, duplicates, len(duplicates)

def dictionary(lacks, duplicates):
    sort_lackes = sorted(lacks)
    sort_duplicates = sorted(duplicates)
    dict = {}
    for i in range(3):
        dict[sort_duplicates[i]] = sort_lackes[i]
    return dict

def converter(matrix, dict):
    for i in range(3):
        for k in range(3):
            n = matrix[i][k]
            if n in dict:
                matrix[i][k] = dict[n]
                dict -= n
    return matrix

base = base_creater()
default_square = read_square()
lacks, duplicates, num_duplicates = gap_founder(default_square, base)
dict = dictionary(lacks, duplicates)
matrix = converter(default_square, dict)

total = 0
for l, d in zip(lacks, duplicates):
    sub = abs(l-d)
    total += sub
print(total)

"""
6*6 hourglass
"""
matrix2D = []
for i in range(6):
    line = list(map(int, input().split()))
    matrix2D.append(line)

max = 0
for x in range(4):
    for i in range(4):
        if i != 3:
            # hourglass = 0
            a = sum(matrix2D[x][i:i+3])
            b = matrix2D[x+1][i+1]
            c = sum(matrix2D[x+2][i:i+3])
            hourglass = a+b+c
            if max < hourglass:
                max = hourglass
        else:
            a = sum(matrix2D[x][3:])
            b = matrix2D[4][4]
            c = sum(matrix2D[x+2][3:])
            hourglass = a+b+c
            if max < hourglass:
                max = hourglass

print(max)
