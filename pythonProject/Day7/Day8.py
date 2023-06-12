# def greet():
#     print("Hello Day 8")
#     print("Hello again")
#     print("What else do you want?")
#
# greet()

# Function that allows for input

# def greet_with_name(name):
#     print(f"Hello Day {name} ")
#     print(f"Hello again {name}")
#     print(f"What else do you want? {name}")
#
# greet_with_name("Oana")

# Function with more then 1 input

# def greet_with(name, location):
#     print(f" My name is: {name} ")
#     print(f"I am from {location}")
#
# greet_with(location="Mosnita Veche", name= "Nick")

import math
#
# test_h = int(input(" Enter height: "))
# test_w = int(input("Enter width: "))
# coverage = 5
#
# def how_many_cans(height, width, cover):
#     area = height*width
#     number_of_cans = math.ceil(area /cover)
#     print(f"You'll need {number_of_cans} cans of paint.")
#
# how_many_cans(height=test_h, width=test_w, cover=coverage)

# Exercise 2 - Prime Numbers

# n = int(input("Enter a number to check: "))

# def prime_checker(number):
#   is_prime = True
#   for i in range(2, number):
#       if number % i == 0:
#           is_prime = False
#   if is_prime:
#       print(f"{number} is a prime number")
#   else:
#       print(f"{number} is not a prime number")
#
# prime_checker(n)