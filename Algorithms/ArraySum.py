numbers = [1, 2, 3, 4, 5]


def array_sum(array):
    sum = 0
    for number in array:
        sum += number
    return sum

print("Suma tablicy:", array_sum(numbers))
