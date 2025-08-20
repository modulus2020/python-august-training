"""Topic Today is Syntax = Print Statements, Indentitation, 
comments, variables, and strings
"""
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

""" 
What are variables?
Variables are used to store data values. In Python, variables 
are created when you assign a value to them. 
They can hold different types of data, 
such as numbers, strings, lists, etc. 
"""
# Examples of variables: Name = "Eric", Age = 20
# Writing Variables = We write variables without quotes, but we assign them values

# Indentation = Indentation is used to define the structure of the code.
# Indentation are used in loops such as for, while, if, else, elseif,
# Indentation is also used in functions and classes.

print("Three is greater than five!")
if 3 < 5:
    print("Three is less than five!")

""" Some examples of variables """
name = "Eric"
age = 20
print("My name is", name, "and I am", age, "years old.")

""" Assignment 
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
"""

first_number = int(input("Enter the first number: "))
secnd_number = int(input("Enter the second number: "))
sum = first_number + secnd_number
print(sum)