"""
29th july 2025
Iplementing for loop
Daliya Daniel
"""

nameList=["Vivian","Salvaion","Daliya","Arib","Harrira","Oluchi"]

print("\n---------------------------------\n")
print(nameList)
print("\n -----------single element")
print(f"welcome to our coding class: {nameList[4]}")
print("\n -----------for names")
for name in nameList:
    print(f"welcome to our coding class:{name}")

    for name in nameList:
        n = input("please enter a name from the list: ").capitalize
        if n is name:
            print(f"You are welcome to coding class: {name}")
            break
        else:
            print("This is an Invalid Name")
            break

for times in range(6):
    n = input("please enter your name here :").capitalize()
    if n in nameList:
        print("welcome to coding class :").capitalize()
    else:
        print("invalid name")
else:
    print("number of attempts is off")



# implementing continue in the for loop 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

age_list=[13,14,9,29,35,89]    
# task1 print out all agse except 29
# task 2 print out correct age 89 from the list if it exists

# task 1
for x in age_list:
    if x ==29:
        continue
    print(x)

# task 2\
for times in range(len(age_list)):
    age = float(input("please enter correct age: "))
    if int(age) in age_list:
        print("wonderful, you have  enter the correct age:",age)
        break
    else:
        print("you have entered an invalid age")
else:
    print("you have exausted the chances")

"""
Assignment:
"""