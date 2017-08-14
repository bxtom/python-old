import sys


def euclid(a, b):
    if a == b:
        return a

    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a


print("Podaj pierwsza liczbe")
a = int(sys.stdin.readline())
print("Podaj druga liczbe")
b = int(sys.stdin.readline())
print("Fibonacci:", euclid(a, b))
