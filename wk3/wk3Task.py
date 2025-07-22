"""
Tasks after the implementation of While and Match/Case with python

1. Implement with 'WHILE' The Typing Speed TestDisplay a sentence to the user and ask them
 to type it exactly. 
 Repeat the prompt until the user types the sentence correctly. Show how many attempts it took.

2. Multi-function CalculatorAsk the user to select an operation: +, -, *, /, or square root. 
Use match-case to determine the action. Accept two numbers for the operation and display the result. 
Handle division by zero where applicable
3. Implement a program that accepts a recharge action: 
i. Buy Airtime ii. Buy Data, iii.Check Balance, iv. Transfer Airtime
Use match-case to respond with mock outcomes based on the user's selection.
4. Implement a Car Rental Cost EstimatorLet the user choose a car type 
(Toyota, Honda, or BMW). Each has a different daily rate. 
Ask how many days they wish to rent the car and calculate the total cost.
5. Implement an Electricity Tariff Billing Based on customer category 
(Residential, Commercial, Industrial), 
apply the appropriate billing rate per unit and calculate total electricity bill for user-inputted unit.
6. Implement  Course Registration SystemPrompt the student to enter a department code 
(CSC, MTH, BIO, ENG). Use match-case to display the full department name and a 
list of example courses available in that department.
# """

# print("Daliya's Project")
# print("")
# print("Good Day")
# name = input("please enter your full name:")
# print("welcome",name,"lets perform some operations")
# print("Lets try some typing tests")
# print("\n")
# sentence="A dog barked at the man and rushed to bite him but the man was clever enough \n to run away into the" \
# "house nearby and asked them to help him with the dog."
# while True:
#  print(sentence)
#  main=str(input("Please type the sentence above:  "))
#  if main.lower()==sentence.lower():
#   print("Correct,Weldone")
#   break
#  else:
#   print("Incorrect, Please try again")

choice = int(input("Select an option:\n1. Buy Airtime\n2. Buy Data\n3. Check Balance\n4. Transfer Airtime\nEnter choice: "))

match choice:
    case 1:
        amount = input("Enter airtime amount: ")
        print("Airtime of","₦",amount, "bought.")
    case 2:
        amount = input("Enter data amount: ")
        print("Data of" ,amount,"GB", "bought.")
    case 3:
        print(" Your account balance: ₦1,500 and data bundle:2.5GB data expires on the 12/dec/2025.")
    case 4:
        number = input("Enter number: ")
        amount = input("Enter amount: ")
        print(amount,"sent to" ,number)
    case _:
        print("Invalid choice.")

print("\n")
print("Welcome to D's Car Rentals")
print("We Offer:\nHonda at ₦1200/day\n Toyota at ₦5000/day\nHonda at ₦6500/day")
honda=1200
toyota=5000
BMW=6500
car= int(input("Please Choose a Car company \n1.Honda \n2.Toyota \n3.BMW\nEnter here:"))
match car:
    case  1:
        days=int(input("For how may days will you be renting this car: "))
        cost=honda*days
        print(f"The price for BMW at",days,"days", "is:",cost)
    case 2:
        days=int(input("For how may days will you be renting this car: "))
        cost=toyota*days
        print(f"The price for BMW at",days,"days", "is:",cost)
    case 3:
        days=int(input("For how may days will you be renting this car: "))
        cost=BMW*days
        print(f"The price for BMW at",days,"days", "is:",cost)
    case _:
        print("Choose from available options")

print("\n")
print("Electricity Tarriff")
print("Customer Categories:\n1. Residential - 209 \n2. Commercial - 4020\n3. Industrial - 70209")
category = int(input("Enter category \n1.Residential, \n2.Commercial, \n3.Industrial\nenter here: "))
units = float(input("Enter number of units to buy: "))

match category:
    case 1:
        rate=209 
        bill = rate* units
        print(f"Total electricitybill for",units,"units","is:",bill)
    case 2:
        rate =4020
        bill = rate* units
        print(f"Total electricitybill for",units,"units","is:",bill)
    case 3:
       rate = 70209
       bill = rate* units
       print(f"Total electricitybill for",units,"units","is:",bill)
    case _:
     print("Invalid category.")

print("\n")
c=str(input("Please your Departmental code e.g\n1.CSC \n2.EEE \n3.MEC \n4.ACC \n5.BAM \nEnter here: "))
match c:
   case c if c=="CSC":
      print("your courses are:\nCSC101-Introduction to Computer Science\nCSC201-Programming with Python\nCSC203-Data Structures and Algorithms" \
      "\nCSC301-operating Systems\nCSC303-Artificial Intelligence")
   case c if c=="EEE":
      print("your courses are:\nEEE101-Introduction to Electrical Engineering\nEEE203-Circuit Theory\nEEE305-Digital Electronics\nEEE407-Power Systems\nEEE409-Control System")
   case c if c=="MEC":
      print("your courses are:\nMEC101-Engineering Drawing\nMEC203-Thermodynamics\nMEC305-Fluid Mechanics\nMEC403-Machine Design\nMEC405-Heat Transfer")
   case c if c=="ACC":
       print("ACC101-Financial Accounting" \
"\nACC201-Cost Accounting"
"\nACC301-Taxation"
"\nACC303-Auditing"
"\nACC401-Management Accounting")
   case c if c=="BAM":
      print("your courses are:BUS101-Principles of Management" \
"\nBUS203-Human Resource Management"
"\nBUS303-Strategic Management"
"\nBUS305-Organizational Behaviour"
"\nBUS40-Business Policy")
   case _:
        print("Invalid Choice")