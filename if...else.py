"""
16th july 2025
Lead:Olatunbosun Adeniyi
9am-11am
Iplementing "if..else" in python
"""

value=int(input("please enter random value between 1 & 20: "))
number=int(value)
name = str(value)
# if value >=10:
#     print("The value is greater than 10 your enter value is", value)
# else:
#     print("The value is less than condition value")

print("\n Iterating long if statements")
if int(value)<=10:
    print("Hi your value/grade is: J")
elif 11<=value and value <=20:
    print("Hi your grade value is: I") 
elif 21<=value and value<=30:
    print("Hi your grade value is :H")
elif 31<=value and value<=40:
    print("Hi your grade value is:G")
elif 41<=value and value<=50:
    print("Hi yor grade value is:F")
elif 51<=value and value<=60:
    print("Hi your grade value is:E")
elif 61<=value and value<=70:
    print("Hi your grade value is:D")
elif 71<=value and value <=80:
    print("Hi your grade value is: C") 
elif 81<=value and value <=90:
 print("Hi your grade value is: B") 
elif 91<=value and value <=100:
 print("Hi your grade value is: A") 
else:
    print("please check your input for correct value")