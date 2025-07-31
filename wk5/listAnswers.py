   
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
while tries<=20:
    student=int(input("Enter student scores: "))
    scoreslist.append(student)
    print(scoreslist)
    tries+=1
    if tries==20:
        break 


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
scoreslist.sort()
scoreslist.pop(5)
scoreslist.pop(9)
scoreslist.pop(17)
print(scoreslist)

print("\n printing 95 if any")
for x in scoreslist:
    if x==95 in scoreslist:
        print("here are those who scored:",x)
    else:
        print("There is no one who scored 95")