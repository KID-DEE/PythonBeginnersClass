"""
user input
using if condition with logic operators
"""
print ("print my name")
#name1 = "samuel"
name1 = input(" please enter your name: ")
print("Hi welcome ",name1)
print("\n lets perform a simple operation")
#simple multiplication
x = float(input("please enter value for x: "))
y = float(input("please enter value for y: "))

result1 = x * y
result2 = int(x) * int(y)
print("Congratulations your result in float is: ", result1)
print("Congratulations your result in integer is: ", result2)

#if condition
print("\n if condition________________________________________________________")
if x > y:
    result = x/y
    print(" Because x is greater than y, Here is a simple division is of x/y: ", result)
else:
    result = x*y
    print("Because x is greater than y, Here is a simple multiplication is of x * y:", result)