"""Topic Today is Syntax = Print Statements, Indentitation, 
comments, variables, and strings

print("Hello World!")

print("450")

print("450 + 50 =")

print(450 + 50)

print("450 + 50 =", 450 + 50)

print("450" + "50")

print("lipstick")

# lip stick ton tea tape garry = lipton, lipstick

# Writing Strings = We write strings in quotes

# Writing Numbers = We write numbers without quotes

 
What are variables?
Variables are used to store data values. In Python, variables 
are created when you assign a value to them. 
They can hold different types of data, 
such as numbers, strings, lists, etc. 


# Examples of variables: Name = "Eric", Age = 20
# Writing Variables = We write variables without quotes, but we assign them values

# Indentation = Indentation is used to define the structure of the code.
# Indentation are used in loops such as for, while, if, else, elseif,
# Indentation is also used in functions and classes.

print("Three is greater than five!")
if 3 < 5:
    print("Three is less than five!")

Some examples of variables
name = "Eric"
age = 20
print("My name is", name, "and I am", age, "years old.")

 Assignment 
1. Write a program that stores your name, age and city in a 
variable and prints them out in one sentnence.

2.Swap the values of two variables without using a third variable.
Example: if x = 10, and y = 20, then after swapping,
x should be 20 and y should be 10.

3. Write a program that takes two numbers as input from the user, 
converts them to integers, and prints their: 
(a) sum.
(b) difference.
(c) product.
(d) quotient.

4. Write a program that takes a string input from the user,
converts it to uppercase, and prints the result.


first_number = int(input("Enter the first number: "))
secnd_number = int(input("Enter the second number: "))
sum = first_number + secnd_number
print(sum)


# DATA TYPES
    hERE ARE SOME COMMON DATA TYPES IN PYTHON:
1. Integers: Whole numbers, e.g., 5, -3, 42
2. Floats: Decimal numbers, e.g., 3.14, -0.001, 2.0
3. Strings: Text enclosed in quotes, e.g., "Hello", 'Python'    
4. Booleans: True or False values
5. Lists: Ordered collections of items, e.g., [1, 2, 3], ["apple", "banana"]

6. Tuples: Immutable ordered collections, e.g., (1, 2, 3), ("a", "b")
7. Sets: Unordered collections of unique items, e.g., {1, 2, 3}, {"apple", "banana"}
8. Dictionaries: Key-value pairs, e.g., {"name": "Alice", "age": 30}
9. None: Represents the absence of a value or a null value  
10. Complex numbers: Numbers with a real and imaginary part, e.g., 3 + 4j
"""

fruits = ["apple", "banana", "cherry", "pawpaw", "orange", "pineapple"]
print(fruits)
# Accessing elements in a list
print(fruits[2])
print(fruits[1])
print(fruits[1:2])
print(fruits[1:3])  # Slicing the list to get a sublist
print(fruits[1:5])

#ASSIGNMENT
# Write a code that can slice through a list of 10 programming languages.
# Rewrite that same code using a Tuple
# Attempt slicing the Tuple like you sliced the List