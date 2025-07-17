print("Daliya's Project")
print("I am your Simple Calculator")
print("Good Day")
name = input("please enter your full name:")
print("welcome",name,"lets perform some operations")
main=int(input("Select Operation: \n1,Addition \n2, Substraction \n3,Multiplication" \
" \n4,Division \n5,Modulus \n6,Floor division \ninput here: "))
try:
    x = int(input("Enter a number:"))
    y = int(input("Enter second number: "))
    if main==1:
        print("Your Result is:",x+y)
    elif main==2: 
        print("Your Result is:",float(x)-float(y))
    elif main==3:
        print("Your Result is:",float(x)*float(y))
    elif main==4:
        print("Your Result is:",float(x)/float(y))
    elif main==5:
        print("Your Result is:",float(x)%float(y))
    elif main==6:
        print("Your result is:",float(x)//float(y))
    else:
        print("Invalid Syntax")
except:ValueError
print("Invalid syntax")