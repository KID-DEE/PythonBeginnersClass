"""
21st july 2025
Lead:Olatunbosun Adeniyi
9am-12noon
Implementing "function" in python 
"""

# # function wit no argument
# def name():
#     print("My name is Daliya")
# name()

# # function with an argument
# def sum(x):
#     print("summation is:", x+20)
# # sum(20)
# print("\n-----------------------")
# def sum2(x):
#     return x+20
# # sum(20)
# print("\n------------------------")
# def sum3(x):
#     result=x+20
#     print(f"result is: {result}")
#     return result
# sum(30)
# print("\n-------------------------")
# # sentence=input("please enter a sentence: ")
# # def whileleops(sentence):
#  while True:
#         print(sentence)
#         main=str(input("Please type the sentence above:  "))
#         if main.lower()==sentence.lower():
#           print("Correct,Weldone")
#           break
#         else:
#           print("Incorrect, Please try again")

# whileleops(sentence)

# classwork
# print("\n")
# print("Welcome to D's Car Rentals")
# print("We Offer:\nHonda at ₦1200/day\n Toyota at ₦5000/day\nHonda at ₦6500/day")
# honda=1200
# # # toyota=5000
# # # BMW=6500
# # car= int(input("Please Choose a Car company \n1.Honda \n2.Toyota \n3.BMW\nEnter here:"))
# def carops():
#     print("\n")
#     print("Welcome to D's Car Rentals")
#     print("We Offer:\nHonda at ₦1200/day\n Toyota at ₦5000/day\nHonda at ₦6500/day")
#     honda=1200
#     toyota=5000
#     BMW=6500
#     car= int(input("Please Choose a Car company \n1.Honda \n2.Toyota \n3.BMW\nEnter here:"))
     
#     match car:
#         case  1:
#             days=int(input("For how may days will you be renting this car: "))
#             cost=honda*days
#             print(f"The price for BMW at",days,"days", "is:",cost)
#         case 2:
#             days=int(input("For how may days will you be renting this car: "))
#             cost=toyota*days
#             print(f"The price for BMW at",days,"days", "is:",cost)
#         case 3:
#             days=int(input("For how may days will you be renting this car: "))
#             cost=BMW*days
#             print(f"The price for BMW at",days,"days", "is:",cost)
#         case _:
#             print("Choose from available options")
# carops()

# print("\n")
# print("Electricity Tarriff")
# print("Customer Categories:\n1. Residential - 209 \n2. Commercial - 4020\n3. Industrial - 70209")
# category = int(input("Enter category \n1.Residential, \n2.Commercial, \n3.Industrial\nenter here: "))
# units = float(input("Enter number of units to buy: "))
# def catops(category):
#     match category:
#         case 1:
#             rate=209 
#             bill = rate* units
#             print(f"Total electricitybill for",units,"units","is:",bill)
#         case 2:
#             rate =4020
#             bill = rate* units
#             print(f"Total electricitybill for",units,"units","is:",bill)
#         case 3:
#             rate = 70209
#             bill = rate* units
#             print(f"Total electricitybill for",units,"units","is:",bill)
#         case _:
#             print("Invalid category.")
# catops(category)

# print("\n")
# c=str(input("Please your Departmental code e.g\n1.CSC \n2.EEE \n3.MEC \n4.ACC \n5.BAM \nEnter here: "))
# def cops(c):
#     match c:
#         case c if c=="CSC":
#             print("your courses are:\nCSC101-Introduction to Computer Science\nCSC201-Programming with Python\nCSC203-Data Structures and Algorithms" \
#       "\nCSC301-operating Systems\nCSC303-Artificial Intelligence")
#         case c if c=="EEE":
#             print("your courses are:\nEEE101-Introduction to Electrical Engineering\nEEE203-Circuit Theory\nEEE305-Digital Electronics\nEEE407-Power Systems\nEEE409-Control System")
#         case c if c=="MEC":
#             print("your courses are:\nMEC101-Engineering Drawing\nMEC203-Thermodynamics\nMEC305-Fluid Mechanics\nMEC403-Machine Design\nMEC405-Heat Transfer")
#         case c if c=="ACC":
#             print("ACC101-Financial Accounting" \
#            "\nACC201-Cost Accounting"
#            "\nACC301-Taxation"
#            "\nACC303-Auditing"
#            "\nACC401-Management Accounting")
#         case c if c=="BAM":
#            print("your courses are:BUS101-Principles of Management" \
#            "\nBUS203-Human Resource Management"
#            "\nBUS303-Strategic Management"
#            "\nBUS305-Organizational Behaviour"
#            "\nBUS40-Business Policy")
#         case _:
#             print("Invalid Choice")
# cops(c)

def projectlist(project):
    numberdays=sum(project)
    valueIndex2=project[2]
    print(f"summation of tasks in a project {project}: {numberdays}\
          value in index 2:",valueIndex2)
    return numberdays,valueIndex2

# hard code the project task
taskdurationlist=[20,10,2,8,10]
projectlist(taskdurationlist)
examtimehours =[2,4,3,2.5,6,]
projectlist(examtimehours)
projectlist([2,4,8,10,20])

#dynamic inputs
#if/else,while,for
task1=int(input("please enter value for task 1: note: int value please:"))
task2=int(input("please enter value for task 2: note: int value please:"))
task3=int(input("please enter value for task 3: note: int value please:"))
task4=int(input("please enter value for task 4: note: int value please:"))
task5=int(input("please enter value for task 5: note: int value please:"))
projectlist([task1,task2,task3,task4,task5])

#full dynamic
