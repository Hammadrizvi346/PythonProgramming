#Taking User Input
name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to the program.")

# Python default input() function always returns a string.
age = input("Enter your age: ")
# To perform arithmetic operations, we need to convert the string input to an integer.  
age = int(age)
next_year_age = age + 1
print("Next year, you will be " + str(next_year_age) + " years old.")
# Alternatively, we can convert the input directly while taking it.
height = float(input("Enter your height in meters: "))
print("Your height is " + str(height) + " meters.")
# Note: Always ensure to handle exceptions for invalid inputs in real-world applications.
# For example, if the user enters a non-numeric value when asked for age or height, it will raise a ValueError.
# Example with exception handling:
age = int(input("Enter your age: "))
print("Next year, you will be " + str(age + 1) + " years old.") 
# Example with exception handling:
# try:
# age = int(input("Enter your age: "))
print("Next year, you will be " + str(age + 1) + " years old.")
# except ValueError:
# print("Please enter a valid number for age.") 
# Example with exception handling:
# try:  
# height = float(input("Enter your height in meters: "))
print("Your height is " + str(height) + " meters.")
