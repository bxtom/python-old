numbers = [17, 24, 13, 77, 88, 11, 55, 7, 3]


def max_value(array):
    result = array[0]
    for number in array:
        if number > result:
            result = number
    return result


def min_value(array):
    result = array[0]
    for number in array:
        if number < result:
            result = number
    return result

print("Max:", max_value(numbers))
print("Min:", min_value(numbers))
