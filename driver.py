"""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Gurshan Dhillon
 ID: gdhill55
File created: October 12, 2024
******************************
this file is the file that will be used to call the main function in login. there is not much happening in this file other than calling the functyion and asking for the min strength
"""
from login import *
# this file is the file used to initiate everything. this is how the computer gets the minimum strength

# below if a input for the what the user wants the min strength to be
min_str = int(input("Enter a minimum strength: "))
# this is code caling the function which is running everything happening
process_password(min_str)
