# 08:09

names = ["Adam", "Roman", "Grzegorz"]
print(names[0])
names[0] = "Anna"
print(names[0])
print(names[1:3])
names[1] = 17
print(names)

animals = ["Dog", "Cat", "Fish"]

all_items = [names, animals]
print(all_items)
print(all_items[0][0])

names2 = names.copy()
print(names2)

names2[0] = "Zenek"
print(names)
print(names2)

names.append("Ewa")
print(names)
print(names.append("Tomek"))
print(names)
names.insert(4, "Stefan")
print(names)
names.remove(17)
print(names)
names.sort()
print(names)
names.reverse()
print(names)
del names[2]
print(names)
all_items2 = names + animals
print(all_items2)
print(len(names))
numbers = [123, 33, 1777, 9]
print(max(numbers))
print(min(numbers))
print(max(names2))
print(all_items2)
