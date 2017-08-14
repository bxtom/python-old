# 19:41

import random

for x in range(0, 10):
    print(x, " ", end="")

print("\n")

names = ["Adam", "Roman", "Grzegorz"]

for n in names:
    print(n)

for x in [2, 4, 6, 8, 10]:
    print(x)

num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])

random_number = random.randrange(0, 100)

while random_number != 15:
    print(random_number)
    random_number = random.randrange(0, 100)

while random.randrange(0, 100) != 15:
    print("nie 15")

i = 0

while i <= 20:
    if i % 2 == 0:
        print(i)
    elif i == 9:
        break
    else:
        i += 1
        continue

    i += 1
