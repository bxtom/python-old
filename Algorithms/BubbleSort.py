import random


def bubble_sort(array):
    is_order_changed = True

    while is_order_changed:
        is_order_changed = False
        for i in range(0, len(array) - 1):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
                is_order_changed = True

    print(array)


array = []
for i in range(0, 10):
    array.append(random.randint(1, 100))

print(array)
bubble_sort(array)
