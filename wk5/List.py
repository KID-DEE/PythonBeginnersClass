# """
# 30th july 2025
# Implementing list manupulation
# Daliya Daniel
# """

# Fruits=["apple","mango","cashew","grape","banana"]

# print(len(Fruits))
# print(type(Fruits))

# print("\n---------------------------")
# print("initial list of fruits")
# print(Fruits)

# print("\n Appending another fruit to the list")

# Fruits.append("cherry")
# print(Fruits)

# print("\n Insert into a list")
# Fruits.insert(2,"pawpaw")
# print(Fruits)

# print("\n Insert new list into a list")
# Fruits.insert(4,["avacado","pine"])
# print(Fruits)


# print("\n pop value from a list")
# Fruits.pop()
# print(Fruits)

# print("\n pop with index number from a list")
# Fruits.pop(-3)
# print(Fruits)


# print("\n delete from a list:")
# Fruits.remove("grape")
# print(Fruits)

studentlist=[]

# while True:
#     student=input("Enter student name: ")
#     studentlist.append(student)
#     print(studentlist)
#     print("\n")


# Classwork
print("\n---------------------------")
tries=0
while tries<=10:
    student=input("Enter student name: ")
    studentlist.append(student)
    print(studentlist)
    tries+=1
    if tries==10:
        break 



    """
    assignment:
    let user be able to create scores for 20 students,
    Tasks
    1.sort the score from highest to lowest
    2.reverse sorting the scores
    3.copy the scoreinto another list 
    4.delete score on the index 5,9,17
    5.printout score 95 if there is any
    """