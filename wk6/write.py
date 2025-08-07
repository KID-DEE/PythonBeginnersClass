"""
Implementing Read from file
Daliya
4th august 2025
python bootcamp
"""

age_list=[]
n=0
while  n<10:
        ageint = int(input("please Enter the age: "))
        age_list.append(ageint)
        n += 1
        # print(age_list)
        print(f"{n} the new age added is {ageint}:")
else:
        print("please age is a number")
        
print("The age list is:", age_list)

f= open("myfiles.txt", "w")

with open("myfiles.txt", "a") as f:
        f.write(str(age_list))
        f.close()


