# Type casting in Python
# Type casting is the conversion of one data type to another data type.
# Type casting is done using built-in functions like int(), float(), str(), etc.
a= "1"
b="2" 
print(a+b) #12
print(int(a)+int(b)) #3

# type casting is two types
# 1. Implicit type casting 
# Example: 
x = 5       # int
y = 2.0     # float
z = x + y   # implicit type casting
print(z)    # 7.0   

# 2. Explicit type casting 
#Example
x = 5       # int
y = 2.0     # float
z = x + int(y)   # explicit type casting
print(z)    # 7
