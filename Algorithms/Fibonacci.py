import sys


def fibonacci(number):
    if number <= 2:
        return 1
    else:
        return fibonacci(number - 2) + fibonacci(number - 1)

print("Podaj liczbe")
print("Fibonacci:", fibonacci(int(sys.stdin.readline())))
