numbers = [17, 24, 13, 77, 88, 11, 55, 13, 3]


def count_occurrences(array, number_to_count):
    counter = 0
    for number in array:
        if number == number_to_count:
            counter += 1
    return counter

print("Liczba wystapien 13:", count_occurrences(numbers, 13))
print("Liczba wystapien 77:", count_occurrences(numbers, 77))
