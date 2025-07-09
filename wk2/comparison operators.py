"""
Comparision operators 
== Equal  x== y
!= Not equal x != y
> Greater than x > y
<  Less than x < y
>= Greater than or equal to x >= y
<= Less than or equal to x <= y

Logical operators
and  x and y
or   x or y
not 

indentity operators
is   x is y
is not  x is not y
in
not in

bitwise operators
&  x & y
|  x | y
"""

# Comparison operators
#== Equal to 
y = "daniel"
z = "daniel" 
print(y>z)
b = 34
c =32
print("checking comparison operator for string value",y == z) 
print("checking comparison operator for integer value",b == c)
print("---------------------------------------------------------------------------------------------\n")
#!= Not equal to
print("checking comparison operator for equal to string : ",y != z)
print("checking comparison operator for not equal to integer : ",b != c)

print("---------------------------------------------------------------------------------------------\n")
#less than
y = "Mike"
z = "Mika"
b = 34
c = 32
print("greater than")
print("comparing greater than value on string  : ",y > z)
print("comparing greater than value on integer : ",b > c)


#classwork
#implement <,>=,<= onthe fpllowing variables
d = 3056
b = 3056
print("---------------------------------------------------------------------------------------------\n")
print("less than")
print("greater than or equal to")
print("less than or equal to")

print("comparing less than value on integer  : ",d < b)
print("comparing greater than or equal to value on integer  : ",d >= b)
print("comparing less than or equal to value on integer  : ",d <= b)

if d < b:
    print("d is less than b")
if d >= b:
    print("d is greater than or equal to b")    
    
    if d <= b:
        print("d is less than or equal to b")

"""
Assignment operators
=
+=
-=
*=
/=
%=
**=  
"""
x = 3
y = 4
#varieble initialization
sum = 0
sum = 0+3
sum =3
sum+= x
print("addition:",sum)
mult =23
mult = mult*3
#mult = 63
print("multiplication:",mult)
modl =20
modl %=3 
print("modulus:",modl)

#classwork
"""
implement the following 1. -=, 2.**=, and 3. /= """ 
#classwork
sub = 10
expotential = 2
division = 5

sub -= 3
print("substarction:",sub)

exp = 23
exp **= 2
print("exponential:",exp)

division /= 2
print("division:",division)