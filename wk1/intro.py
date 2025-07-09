"""
2nd july 2025
Class 3 
syntax, variables, data types, 
"""

#syntax is a machine readable word or statements
print("my name id : paul")

#variable definition
name1 = "samuel" #asigning name samuell to name1 is in quotation because it is a string
num = 3 #asigning 3 to num and this is an integer no need for quotation
num2 = 23.03859485 #asigning number with decimal place to num2 and this is a float with no need for quotation
print(num2)
_num3 = 2/4
numfraction = 4/5
print(_num3)

#list
genderlist = ["male", "female"]
namelist = ["samuel, daliya, aribb, vivian, salvation"]
numlist = [ 23, 24, 25, 26, 90]
print(numlist)
#dictionary
schoolDict = {"name": "nigerian navy military school", "location": "dougirei", "founded": 2000, "founder": "navy"}
personDict = {"name" :"daliya","location": "dougirei","school": "nigerian navy military school", "gender" : "male", "age": 13}
print(personDict)

#data types integer, float, string, list, dictionary
#construct 2 new variables of each of the list, dictionary, float, string explained data types 

#classworkk
Dal1 = "daliya"
_dal_2= "daniel"
print(Dal1,_dal_2)
symlist = ["!, @, #, $, %"]
classlist = ["class 3", "class 4", "class 5"]
print(symlist, classlist)
MIHdict = {"name": "mentors innovators hub", "location": "Bank road, yola", "description": "training hub for young innovators", "founded": 2008, "founder": "Mr. OLa"}
MAUdict = {"name" : "modibo adama university", "location": "yola, adamawa state", "founded": 2012, "founder": "modibo adama", "description": "a university in yola adamawa state"}
print(MIHdict, MAUdict)
_flt1 = 3.14    
_flt2 = 2.71
print(_flt1, _flt2) 

#LIST MANIPULATION
namelist = ["samuel", "daliya", "aribb", "vivian", "salvation"]
#numbering = [ 1,     2,      3,      4,         5]
#Post/index = [0,       1,      2,     3,      4]

print("name is :", namelist[2],)
condition = True
condition2 = False

#type(name1) get the type of a variable
#len()count the character or list of a variable

#verify the data types
print("checking the data type of", {name1},":::",type(name1)) 
print("checking the data type of", namelist,":::",type(namelist))

#classwork
#verify the data type for num, num1, genderlist, schoolDict, persondict, condition, condition2.
print("checking the data type of", num,":::",type(num))
print("checking the data type of", num2,":::",type(num2))
print("checking the data type of", genderlist,":::",type(genderlist))
print("checking the data type of", schoolDict,":::",type(schoolDict))
print("checking the data type of", personDict,":::",type(personDict))
print("checking the data type of", condition,":::",type(condition))
print("checking the data type of", condition2,":::",type(condition2))