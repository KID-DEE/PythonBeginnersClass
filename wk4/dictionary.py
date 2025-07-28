sams={
    'name':'samuel',
    'age' : 23,
    'sex':'male',
    'complexion':'light',
    'height': 1.75,
    'origin':"anambra",
    'residency':"anambra"
}
#read element
print(sams)
#return the data types
print(type(sams))

#reading only values
print("getting only values:",sams.values())
print("getting only values: ",sams.get('name'))

#reading only keys

#update a value using an element 
print("printing out value using dictionary key V1: ",sams['age'])
print("printing out value using dictionary key V2: ",sams.get('age'))