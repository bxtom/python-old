# 26:57

long_string = "This document gives coding conventions for the Python code"
print(long_string[0:4])
print(long_string[-4:])
print(long_string[:-5])
print("Good " + long_string[-4:])
print("%c is my %s letter and my number %d number is %.5f" %
      ("X", "favorite", 1, .14))
print(long_string.upper())
print(long_string.find("document"))
print(long_string.isalpha())
print(long_string.isalnum())
print(long_string.replace("document", "book"))
print(long_string.strip())
quote_list = long_string.split(" ")
print(quote_list)
