import sys


def get_absolute_value(number):
    if number >= 0:
        return number
    else:
        return -number

print("Podaj liczbe")
print("Wartosc bezwzgledna podanej liczby to:", get_absolute_value(int(sys.stdin.readline())))
