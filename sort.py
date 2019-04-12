
"""
Rule


"""

def input_loader():
    num = int(input)
    arr = list(map(int, input().split())
    return num, arr

def buble_sort(list):
    for i in range(0, len(list)-1):
        for k in range(0, len(list)-1-i):
            if arr[k] > arr[k+1]:
                arr[k+1] = arr[k]
                arr[k] = arr[k+1]
            else:
                break

max, arr = input_loader()
# counter = 0
updated_arr = None
for _ in range(max):
    result = buble_sort(arr)
    updated_arr = result

sys.stdout.write("Array is sorted in " + str(max) + " swaps.")
sys.stdout.write("\n")
sys.stdout.write("First Element: " + str(updated_arr[0]))
sys.stdout.write("\n")
sys.stdout.write("Last Element: " + str(updated_arr[-1]))



import sys

num = int(input)
arr = list(map(int, input().split()))
swapped = True
swaps = 0

while swapped:
    swapped = False
    for idx, val in enumerate(arr[:-1]):
        if val > arr[idx+1]:
            arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
            swapped = True
            swaps += 1

sys.stdout.write("Array is sorted in " + str(swaps) + " swaps.")
sys.stdout.write("\n")
sys.stdout.write("First Element: " + str(arr[0]))
sys.stdout.write("\n")
sys.stdout.write("Last Element: " + str(arr[-1]))

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

total = 0
for i in range(n):
    numberOfSwaps = 0
    for j in range(n-1):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
            numberOfSwaps += 1
    if numberOfSwaps == 0 :
        break
    total += numberOfSwaps

print("Array is sorted in",total,"swaps.")
print("First Element:",a[0])
print("Last Element:",a[n-1])
