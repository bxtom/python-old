import random


def quick_sort(array, lo, hi):
    if lo < hi:
        p = partition(array, lo, hi)
        quick_sort(array, lo, p - 1)
        quick_sort(array, p + 1, hi)


def partition(array, lo, hi):
    pivot = array[hi]
    i = lo - 1
    for j in range(lo, hi):
        if array[j] < pivot:
            i += 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

    if array[hi] < array[i + 1]:
        temp = array[i + 1]
        array[i + 1] = array[hi]
        array[hi] = temp

    i += 1

    return i


array = []
for i in range(0, 10):
    array.append(random.randint(1, 100))

print(array)
quick_sort(array, 0, len(array) - 1)
print(array)
