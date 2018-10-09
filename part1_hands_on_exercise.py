"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print ("The Pi value is ", pi, "and the type is", type(pi))

# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i < 50:
    print("i is less than 50")
elif i > 50:
    print ("i is greater than 50")
else:
    print ("i is equal to 50")     


# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit == 'orange':
    print("The fruit picked is ", picked_fruit, " and its colour is orange")
elif picked_fruit == 'strawberry':
    print("The fruit picked is ", picked_fruit, " and its colour is red")
elif picked_fruit == 'banana':
    print("The fruit picked is ", picked_fruit, " and its colour is yellow")

# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def mul_two_num (a,b):
    c = a*b
    return c

# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =",mul_two_num (12,96))

print("48 x 17 =",mul_two_num (48,17))

print("196523 x 87323 =",mul_two_num (196523,87323))
