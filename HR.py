


knn = neighbors.KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
accuracy_score(y_test, y_pred)





import sys
for i in range(10):
    // どんどんと行に追記していく.
    sys.stdout.write("*")
    sys.stdout.flush()
    time.sleep(0.1)
print()

"""
**********
"""

from sys import stdin
lines = stdin.read().splitlines()

my_input = input()
while(len(my_input)>0):
    #Do whatever you want
    my_input=input()  #take ne


import sys

def main():
    if sys.stdout.isatty():
        print('もしや、出力先はターミナルですね。')
    else:
        print('出力先はターミナルではありませんね。')


if __name__ == '__main__':
    main()


sys.stdout.write("YES")
sys.stdout.write("\n")
sys.stdout.flush()

while True:
  try:

  except (EOFError):
    break #end of file reached
