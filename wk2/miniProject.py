"""
Mini Project after the completion of comments, Variable, Operators[Arithmetics, Comparison,
Logic, Assignment], simple if-else.
"""

"""
1. Declare a variable called "name" to store your first name and print a greeting with it.
2. Create two variables x and y and store any two numbers. Print the sum of x and y.
3. Using the same variables x and y, print their difference.
4. Multiply the two variables and store the result in a new variable called product. Print the result.
5. Divide x by y and print the result.
6. Create a variable age and assign your age. Check if the age is greater than or equal to 18 and print the result.
7. Create two variables math_score and english_score, each with values between 0 and 100. Check if both are above 50 and print True or False.
8. Create a variable is_logged_in and set it to True. Use a logical NOT to print the opposite value.
9. Declare a variable is_raining as True and has_umbrella as False. Use logical OR to determine if you can go outside and print the result.
10. Create a variable number and assign any integer. Check if the number is even using the modulo operator and print True or False.
11. Create a variable score and set it to a value between 0 and 100. Use an if-else statement to print "Pass" if the score is 50 or above and "Fail" otherwise.
12. Declare a variable temp for temperature and check if it is above 30. If so, print "Hot", otherwise print "Cool".
13. Assign a value to a variable count. Add 10 to it using the assignment operator and print the updated value.
14. Set two variables a and b. Check if a is not equal to b and print the result.
15. Declare a variable status and set it to "active". Use an if-else to print "Welcome" if status is "active", otherwise print "Access denied".
16. Create a variable time and assign a value in 24-hour format. If time is less than 12, print "Good morning", else print "Good afternoon".
17. Declare two numbers m and n. Swap their values using a third variable and print the result.
18. Create a variable marks and use an if-else to check if marks are greater than 80. Print "Excellent" if true, else print "Keep trying".
19. Assign values to two variables p and q. Check if both are divisible by 2 and print the result.
20. Ask the student to choose any real-life decision (e.g., choosing what to eat) and use a simple if-else structure to model it in code
"""


print("Daliya's Project")#this is from no.1
print("Good Day")
name = input("please enter your full name:")
print("welcome",name,"lets perform some operations")
x = input("enter your first value:")
y =  input("enter second value:")
print( "Result for Addition =",int(x) + int(y))
Difference = int(x) - int(y)
print ("Result of Difference =",Difference)
product = float(x)*float(y)
print("Result of Product is",int(product))
print ("Result for Division =",int(x)/int(y) )#to no.5
print("\n")
age = int(input("please enter you age:"))
if age > 18:
    print("You are an Adult")
else:
    print("You are a Minor")#no.6
print("\n")
math_score= int(input("please enter Maths score:"))
english_score = int(input("please enter English score:"))
if math_score >50:
    print("You have passed ")
else:
    print("You have failed, try again next year")
if english_score >50:
    print("You have passed ")
else:
 print("You have failed, try again next year")#no.7
print("\n")
is_logged_in = True
print("is not logged in:",not is_logged_in )
is_raining = True
has_umbrella = False
print("can i go out:", is_raining or has_umbrella )#no.8
print("\n")
score = int(input("please enter score:"))
if score > 50:
    print("pass")
else:
    print("fail")
    print("\n")
temp= int(input("please enter temperature:"))
if temp > 30:
    print("Hot")
else:
    print("Cool")
print("\n")
count =int(input("please enter number:"))
count+=10
print(count)
print("\n")
a = int(input("please enter number:"))
b = int(input("please enter number:"))
if a == b:
    print("they are equal")
else:
    print("thet are not equal")
    print("\n")
status= input("please choose if you are active or not:")
if status =="active":
    print("Welcome")
else:
    print("Access denied")
print("\n")
time= int(input("what time is it?"))
if time<1200:
    print("good morning")
elif time>=1200:
    print("good afternoon")
elif time >=1600:
    print("good evening" )
else:
    print("good night")
print("\n")
m= input("enter number:")
n= input("please enter number:")
print("m =", m)
print("n =", n)
print(m)
print(n)

q = m
m = n
n = q
print("m =", m)
print("n =", n)

print("\n")
marks = int(input("please enter mark:"))
if marks>80:
    print("excellent")
else:
    print("keep trying")
print("\n")
p =int(input("please enter number:"))
q =int(input("please enter number:"))
u = p/2
k = q/2
if u==0 and k == 0:
    print("true")
else:
    print("false")
    print("\n") 
question =input("what do you want to do:1.eat    2.sleep   3.go outside   4.play games  5.exercise = ")
if  question == '1':
    print("okay goodbsdvcjashye")
elif question=="2":
    print("alrigt, see you next time")
elif question=="3":
    print("okay goodbye")
elif question=="4":
    print("okay goodbye")
elif question=="5":
    print("alrigt, see you next time")
else:
    print("hmmmm..... nawa 4 u oooohh")

    