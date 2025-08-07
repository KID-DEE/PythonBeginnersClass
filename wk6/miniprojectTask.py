
print("Daliya's Project")#this is from no.1
print("Good Day")
name = input("please enter your full name:")
print("welcome",name,"lets perform some operations")
with open("MiniProjectTaskSolutions.txt", "x") as f:
    str(name)
    f.write(f"print Daliyas Project\n Good Day{name}\n  welcome {name} lets perform some operations")
    f.close()


x = input("enter your first value:")
y =  input("enter second value:")
result=int(x)+int(y)
print( "Result for Addition =",int(result))
str(result)
with open("mini project task solutions.txt", "a") as f:
    f.write( f"\nResult for Addition ={result}")
    f.close()


Difference = int(x) - int(y)
print ("Result of Difference =",Difference)
str(Difference)
with open("mini project task solutions.txt", "a") as f:
    f.write(f"\nResult of Difference = {Difference}")
    f.close


product = float(x)*float(y)
print("Result of Product is",int(product))
str(product)
with open("mini project task solutions.txt", "a") as f:
    f.write(f"\nResult of Multiplication = {product}")
    f.close()


divison=int(x)/int(y)
print ("Result for Division =",divison)
str(divison)
with open("mini project task solutions.txt", "a") as f:
    f.write(f"\nResult of division = {divison}")
    f.close()


print("\n")
age = int(input("please enter you age:"))
if age >= 18:
    print("You are an Adult")
    with open("mini project task solutions.txt", "a") as f:
        f.write("\nYou are an Adult")
else:
    print("You are a Minor")
    with open("mini project task solutions.txt", "a") as f:
        f.write("\nYou are a Minor")
str(age)
with open("mini project task solutions.txt", "a") as f:
    if age >= 18:
        f.write("\nYou are an adult")
    else:
        f.write("\nYou're a minor")    
    f.close()
print("\n")
math_score= int(input("please enter Maths score:"))
english_score = int(input("please enter English score:"))
if math_score >=50:
    print("You have passed ")
    with open("mini project task solutions.txt", "a") as f:
        f.write("\nYou have passed Maths")
else:
    print("You have failed, try again next year")
    with open("mini project task solutions.txt", "a") as f:
        f.write("\nYou have failed Maths, try again next year")
if english_score >=50:
    print("You have passed ")
    with open("mini project task solutions.txt", "a") as f:
        f.write("\nYou have passed English")
else:
 print("You have failed, try again next year")
 with open("mini project task solutions.txt", "a") as f:
     f.write("\nYou have failed English, try again next year")
with open("mini project task solutions.txt","a") as f:
    if math_score>=50:
        f.write("\nYou have passed ")
    else:
        f.write("\nYou have failed, try again next year")
    if english_score >=50:
        f.write("\nYou have passed ")
    else:
        f.write("\nYou have failed, try again next year")
    f.close()

print("\n")
is_logged_in = True
with open("mini project task solutions.txt", "a") as f:
    f.write(f"\nis not logged in:{not is_logged_in}")
is_raining = True
has_umbrella = False
with open("mini project task solutions.txt", "a") as f:
    f.write(f"\ncan i go out: {is_raining or has_umbrella}") #no.8
print("\n")
score = int(input("please enter score:"))
if score > 50:
    print("pass")
    with open("mini project task solutions.txt", "a") as f:
        f.write("\npass")
else:
    print("fail")
    with open("mini project task solutions.txt", "a") as f:
        f.write("\nfail")
    print("\n")
temp= int(input("please enter temperature:"))
if temp > 30:
    print("Hot")
    with open("mini project task solutions.txt", "a") as f:
        f.write("\nHot")
else:
    print("Cool")
    with open("mini project task solutions.txt", "a") as f:
        f.write("\nCool")
print("\n")
count =int(input("please enter number:"))
count+=10
print(count)
print("\n")
a = int(input("please enter number:"))
b = int(input("please enter number:"))
if a == b:
    print("they are equal")
    with open("mini project task solutions.txt", "a") as f:
        f.write("\nthey are equal")
else:
    print("thet are not equal")
    with open("mini project task solutions.txt", "a") as f:
        f.write("\nthey are not equal")
    print("\n")
status= input("please choose if you are active or not:")
if status =="active":
    print("Welcome")
    with open("mini project task solutions.txt", "a") as f:
        f.write("\nWelcome")
else: 
    print("Access denied")
    with open("mini project task solutions.txt", "a") as f:
        f.write("\nAccess denied")
print("\n")
time= int(input("what time is it?"))
if time<1200:
    print("good morning")
    with open("mini project task solutions.txt", "a") as f:
        f.write("\ngood morning")
elif time>=1200:
    print("good afternoon")
    with open("mini project task solutions.txt", "a") as f:
        f.write("\ngood afternoon")
elif time >=1600:
    print("good evening" )
    with open("mini project task solutions.txt", "a") as f:
        f.write("\ngood evening")
else:
    print("good night")
    with open("mini project task solutions.txt", "a") as f:
        f.write("\ngood night")
print("\n")
m= input("enter number:")
n= input("please enter number:")
print("m =", m)
print("n =", n)
print(m)
print(n)

q = m
m = n

print("\n")
marks = int(input("please enter mark:"))
print("m =", m)
print("n =", n)
with open("mini project task solutions.txt", "a") as f:
    f.write(f"\nm = {m}\nn = {n}")
if marks>80:
    print("excellent")
    with open("mini project task solutions.txt", "a") as f:
        f.write("\nexcellent")
else:
    print("keep trying")
    with open("mini project task solutions.txt", "a") as f:
        f.write("\nkeep trying")
print("\n")
p =int(input("please enter number:"))
q =int(input("please enter number:"))
u = p/2
k = q/2
if u==0 and k == 0:
    print("true")
    with open("mini project task solutions.txt", "a") as f:
        f.write("\ntrue")
else:
    print("false")
    with open("mini project task solutions.txt", "a") as f:
        f.write("\nfalse")
    print("\n") 
question =input("what do you want to do:1.eat    2.sleep   3.go outside   4.play games  5.exercise = ")
if  question == '1':
    print("okay goodbsdvcjashye")
    with open("mini project task solutions.txt", "a") as f:
        f.write("\nokay goodbsdvcjashye")
elif question=="2":
    print("alrigt, see you next time")
    with open("mini project task solutions.txt", "a") as f:
        f.write("\nalrigt, see you next time")
elif question=="3":
    print("okay goodbye")
    with open("mini project task solutions.txt", "a") as f:
        f.write("\nokay goodbye")
elif question=="4":
    print("okay goodbye")
    with open("mini project task solutions.txt", "a") as f:
        f.write("\nokay goodbye")
elif question=="5":
    print("alrigt, see you next time")
    with open("mini project task solutions.txt", "a") as f:
        f.write("\nalrigt, see you next time")
else:
    print("hmmmm..... nawa 4 u oooohh")
    with open("mini project task solutions.txt", "a") as f:
        f.write("\nhmmmm..... nawa 4 u oooohh")