"""
16th july 2025
Lead:Olatunbosun Adeniyi
9am-11am
Iplementing "Match Case" in python
"""

value=int(input("please enter your value: "))

day = int(input("Select day:\n 1:Sunday \n 2:Monday \n 3:Tuesday \n 4:Wednesday \n 5:Thursday" \
" \n 6:Friday \n 7: Saturday:"))

match day:
    case day if day==1:print("Sunday")
    case 2:print("Monday")
    case 3:print("Tuesday")
    case 4:print("Wednesday")
    case 5:print("Thursday")
    case 6:print("Friday")
    case 7:print("Saturday")
    case _:print("Invalid")
#implement the earlier if-else
# if value <=10
match value:
    case value if value<=10:
      print("Your value is less than 10: J")
    case value if 11<=value and value <=20:
     print("Your value is less than 10: I")
    case _:
     print("Wrong value please enter right")
      