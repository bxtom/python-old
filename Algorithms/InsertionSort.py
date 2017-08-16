import random


def insertion_sort(array):
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            for j in range(i, 0, -1):
                if array[j] < array[j - 1]:
                    temp = array[j]
                    array[j] = array[j - 1]
                    array[j - 1] = temp
    print(array)


array = []
for i in range(0, 10):
    array.append(random.randint(1, 100))

print(array)
insertion_sort(array)
