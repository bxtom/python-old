import sys


def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)

print("Podaj liczbe")
print("Silnia:", factorial(int(sys.stdin.readline())))
