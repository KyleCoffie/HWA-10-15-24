# 2. User Input Data Processor
# Objective: The aim of this assignment is to process and format user input data.

# Task 1: Input Length Validator Write a script that asks for and checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.

first_name = input("What is your first name? ")
last_name= input("What is your last name? ")

first = len(first_name)
last = len(last_name)
if first <= 2 or last <= 2:
    print("Sorry your name is to short for the program")
else:
    print (first)
    print (last)