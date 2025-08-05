# All file writing statements from miniprojectTask.py

# Variable definitions for demonstration

name = input("Enter your name: ")
result = int(input("Enter result for addition: "))
Difference = int(input("Enter result for difference: "))
product = int(input("Enter result for multiplication: "))
divison = int(input("Enter result for division: "))
age = int(input("Enter your age: "))
math_score = int(input("Enter your Maths score: "))
english_score = int(input("Enter your English score: "))
is_logged_in = True
is_raining = False
has_umbrella = False
m = input("Enter value for m: ")
n = input("Enter value for n: ")


with open("mini project task solutions.txt", "x") as f:
    str(name)
    f.write(f"print Daliyas Project\n Good Day{name}\n  welcome {name} lets perform some operations")
    f.close()

with open("mini project task solutions.txt", "a") as f:
    f.write( f"\nResult for Addition ={result}")
    f.close()

with open("mini project task solutions.txt", "a") as f:
    f.write(f"\nResult of Difference = {Difference}")
    f.close

with open("mini project task solutions.txt", "a") as f:
    f.write(f"\nResult of Multiplication = {product}")
    f.close()

with open("mini project task solutions.txt", "a") as f:
    f.write(f"\nResult of division = {divison}")
    f.close()

with open("mini project task solutions.txt", "a") as f:
    f.write("\nYou are an Adult")
with open("mini project task solutions.txt", "a") as f:
    f.write("\nYou are a Minor")
with open("mini project task solutions.txt", "a") as f:
    if age >= 18:
        f.write("\nYou are an adult")
    else:
        f.write("\nYou're a minor")    
    f.close()
with open("mini project task solutions.txt", "a") as f:
    f.write("\nYou have passed Maths")
with open("mini project task solutions.txt", "a") as f:
    f.write("\nYou have failed Maths, try again next year")
with open("mini project task solutions.txt", "a") as f:
    f.write("\nYou have passed English")
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
with open("mini project task solutions.txt", "a") as f:
    f.write(f"\nis not logged in:{not is_logged_in}")
with open("mini project task solutions.txt", "a") as f:
    f.write(f"\ncan i go out: {is_raining or has_umbrella}") #no.8
with open("mini project task solutions.txt", "a") as f:
    f.write("\npass")
with open("mini project task solutions.txt", "a") as f:
    f.write("\nfail")
with open("mini project task solutions.txt", "a") as f:
    f.write("\nHot")
with open("mini project task solutions.txt", "a") as f:
    f.write("\nCool")
with open("mini project task solutions.txt", "a") as f:
    f.write("\nthey are equal")
with open("mini project task solutions.txt", "a") as f:
    f.write("\nthey are not equal")
with open("mini project task solutions.txt", "a") as f:
    f.write("\nWelcome")
with open("mini project task solutions.txt", "a") as f:
    f.write("\nAccess denied")
with open("mini project task solutions.txt", "a") as f:
    f.write("\ngood morning")
with open("mini project task solutions.txt", "a") as f:
    f.write("\ngood afternoon")
with open("mini project task solutions.txt", "a") as f:
    f.write("\ngood evening")
with open("mini project task solutions.txt", "a") as f:
    f.write("\ngood night")
with open("mini project task solutions.txt", "a") as f:
    f.write(f"\nm = {m}\nn = {n}")
with open("mini project task solutions.txt", "a") as f:
    f.write("\nexcellent")
with open("mini project task solutions.txt", "a") as f:
    f.write("\nkeep trying")
with open("mini project task solutions.txt", "a") as f:
    f.write("\ntrue")
with open("mini project task solutions.txt", "a") as f:
    f.write("\nfalse")
with open("mini project task solutions.txt", "a") as f:
    f.write("\nokay goodbsdvcjashye")
with open("mini project task solutions.txt", "a") as f:
    f.write("\nalrigt, see you next time")
with open("mini project task solutions.txt", "a") as f:
    f.write("\nokay goodbye")
with open("mini project task solutions.txt", "a") as f:
    f.write("\nokay goodbye")
with open("mini project task solutions.txt", "a") as f:
    f.write("\nalrigt, see you next time")
with open("mini project task solutions.txt", "a") as f:
    f.write("\nhmmmm..... nawa 4 u oooohh")
