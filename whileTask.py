"""
**Class Work: Python Control Flow Applications**

---

# ### **Group A: While Loop Tasks**

# **1. Number Guessing Game**
# Write a program where the computer selects a random number between 1 and 20. The user has 5 attempts to guess the correct number. Provide feedback for each guess ("Too high" or "Too low"). End the game early if guessed correctly.

# **2. Password Strength Validator**
# Ask the user to enter a password. Continue prompting until the password:

# * Is at least 8 characters long
# * Includes at least one digit
# * Includes at least one uppercase letter

# **3. ATM Simulation**
# Create a menu-driven ATM interface where the user can:

# * Withdraw money (check that balance is sufficient)
# * Deposit money
# * Check balance
# * Exit the program

# Repeat this menu until the user chooses to exit.
# """


# Answers

print("Daliya's Project")#this is no.1
print("Good Day")
name = input("please enter your full name:")
print("welcome",name,"lets play a game:")
number = 11
print("I'm thinking of a number between 1 and 20.")
print("You have 5 attempts to guess it.")
tries = 0
while tries < 5:
    guess = int(input("Guess a number (1-20): "))
    if guess == number:
        print("correct!")
        break
    elif guess < number:
        print("Too low.")
    else:
        print("Too high.")
    tries += 1

if guess!= number:
    print("Sorry, the number was", number)
print("\n no.2")
password = "Dali2000"
while True:
    num =str(input("please enter your password:"))
    if num ==password:
        print("welcome user")
        break
    else:
        print("wrong password \n please try again")
print("\n no.3")
balance =100000
we =2
while we<=2:
  print("\n1. Withdraw")
  print("2. Deposit")
  print("3. Check Balance")
  print("4. Exit")

  choice = input("Enter choice: ")
  if choice == '1':
   amount = int(input("Withdraw amount: "))
   if amount <= balance:
            balance -= amount
            print("your account balance is : ",balance)
  elif choice == '2':
        amount = int(input("Deposit amount: "))
        balance += amount
        print("your acount balance is: ",balance)

  elif choice == '3':
    print("Balance:", balance)
  elif choice == '4':
   break
