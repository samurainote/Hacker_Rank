



# toys and budget

num_toys, budget = map(int, input().split())
prices = list(map(int, input().split()))
basket = []
for p in prices:
    if budget >= p:
        basket.append(p)

basket.sort()
total = 0
counter = 0
while total <= budget:
    for p in basket:
        total += p
        counter += 1

print(counter)
