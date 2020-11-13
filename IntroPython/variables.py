#!/usr/bin/env python
# variables.py
# A variable containing a string
name = 'Chuck Roesel'

# A variable containing an integer
age = 56

# A list of strings
names = ["Patsy Stone", "Edina Monsoon", "Saffron Monsoon"]

# A list of numbers
numbers = [15.5, 25.6, 50, 500]

# A dictionary of names and ages
ages = {'Chuck': 56, 'Patsy': 61, 'Edina': 58}

# Print the values of the variables
print(name)
print(age)
print(names)
print(numbers)
print(ages)

# Find out what type Python assigned to the variables
print(type(name))
print(type(age))
print(type(names))
print(type(numbers))
print(type(ages))

# Iterate over names in a for loop
for name in names:
        print(name)
        print(type(name))
