# 13:38

names = {"Adam": 1,
         "Adolf": 2,
         "Anna": 3,
         "Agnieszka": 4}

print(names["Adam"])
print(names)
names["Anna"] = 7
print(names)
del names["Adolf"]
print(names)
print(names.get("Adam"))
print(names.keys())
print(names.values())
