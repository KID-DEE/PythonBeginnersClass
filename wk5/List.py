"""
30th july 2025
Implementing list manupulation
Daliya Daniel
"""

Fruits=["apple","mango","cashew","grape","banana"]

print(len(Fruits))
print(type(Fruits))

print("\n---------------------------")
print("initial list of fruits")
print(Fruits)

print("\n Appending another fruit to the list")

Fruits.append("cherry")
print(Fruits)

print("\n Insert into a list")
Fruits.insert(2,"pawpaw")
print(Fruits)

print("\n Insert new list into a list")
Fruits.insert(4,["avacado","pine"])
print(Fruits)


print("\n pop value from a list")
Fruits.pop()
print(Fruits)

print("\n pop with index number from a list")
Fruits.pop(-3)
print(Fruits)


print("\n delete from a list:")
Fruits.remove("grape")
print(Fruits)

