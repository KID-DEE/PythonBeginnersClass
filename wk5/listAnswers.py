   
"""
    assignment:
    let user be able to create scores for 20 students,
    Tasks
    1.sort the score from highest to lowest
    2.reverse sorting the scores
    3.copy the score into another list 
    4.delete score on the index 5,9,17
    5.printout score 95 if there is any
"""
scoreslist=[]
tries=0
num=int(input("How many students do you want to enter their scores:"))
while tries<=num:
    try:
        student=int(input("Enter student scores: "))
        scoreslist.append(student)
        print(scoreslist)
        tries+=1
        if tries==num:
            break 
    except ValueError:
        print("Please enter number")

print("\n Sorting the list")
scoreslist.sort()
print(scoreslist)

print("\n Reverse sorting for scores")
scoreslist.reverse()
print(scoreslist)

print("\ncopying scores into another list")
newlist=scoreslist[:]
print(newlist)

print("\n Deleting scores on index 5,9,17")
index=int(input("Please enter your value to remove: "))
num2=int(input("Please enter the number of scores: "))
if index < num2:
    scoreslist.remove(index)
else:
    print("Index out of range")

print("\n printing 95 if any")
x=int(input("please enter what score to print: ")) 
if x in scoreslist:
    print("this is the score:",x)
else:
    print("There is no one who scored",x)


