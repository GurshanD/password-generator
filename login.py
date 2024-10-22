"""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Gurshan Dhillon
 ID: gdhill55
File created: October 12, 2024
******************************
this file is the file used to ask the user for their password or if they want a random one. this file also checks if the password is strong enough(strength is measuered by the table in the assignmebt pdf. it also tells the user if their password is acceptable. this file also takes functions from 2 other files.)
"""
from password import *
from generate import *

# this function taeks care of the process of  getting a password checking its strength and making sure its strength is more than the requirment
def process_password(min_strength):

    # this loop will keep asking for a new password until one that meets the strength requirement is entered
    while True:
        # ask the user for input. if they want a random password, they can type 'X', otherwise, they can enter their own
        user_input = input("Type in a new password or type X for a randomly generated password: ")

        # if the user types 'X', generate a random password of 15 characters
        if user_input.lower() == 'x':
            password = generate_password(15)
            strength = password_strength(password)  # check the strength of the generated password
            print(f"Your password: {password}")
            print(f"Your password has the strength of {strength}")
        else:
            # if the user enters their own password, use that and check its strength
            password = user_input
            strength = password_strength(password)
            print(f"Your entered: {password}")
            print(f"Your password has the strength of {strength}")

        # if the password strength is equal to or greater than the minimum required, break the loop
        if strength >= min_strength:
            print("Password is strong enough.")
            break  # stop the loop if the password meets the strength requirement
        else:
            # if the password isn't strong enough, let the user know and ask for another password
            print("Your password is not strong enough. Please create a new password that is stronger.")
