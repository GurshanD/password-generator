"""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Gurshan Dhillon
 ID: gdhill55
File created: October 12, 2024
******************************
this file is the file that the user will be using to make the random password(if they decde to input x when prompted. This password will always contain 15 characters)
"""

import random
# this file is the file that will be used to create teh random password of 15 characters. (when the user types x)

# here we are defining the function
def generate_password(length):
    password=""
    # this is not a list, insted it is just a single string full of all of the possible options that the random password can contain
    ALL_CHARS = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*/?-+=,.|~")

    # this is the for looop which creates the password.
    for i in range(length):
        password += random.choice(ALL_CHARS)

    return password
