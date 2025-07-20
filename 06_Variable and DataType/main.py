print("Variable and Datatypes")

# Variable 
# Variable is like a Container that holds the Data. Creating a variable is like creating a Placeholder and assigning it a value.
# ex -
A = 2
# A is a variable which contains a value of 2

# DataType 
# Datatype specifies the type of Data which was stored in a variable, we can use type(@) to fine the type of any datatype
print(type(A))

# Types of dataType

# Numeric 
a = 12 # int 
b = 12.4 # float
c = complex(12+3) # complex
print( type(a), type(b), type(c))

# Text
# string
print("Stirng")

# Boolean 
# consist true or false

# Sequenced Data
# list - Collection of Data 
list1 = [1, 2.6, ["Nishu" , "Nilesh"] , [4, -92]]
print(list1)
# typle - ccollection of Data but Immutable 
tuple1 = (("Apple, Bannana") , ("Peach", "Orange"))
print(tuple1)

# Mapped Data 
# collection of Data containing a key value pair 
dict1 = {
    "Name" : "Nilesh", 
    "Age" : 23,
    "Designation" : "Developer"
}
