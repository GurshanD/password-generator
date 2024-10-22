"""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Gurshan Dhillon
 ID: gdhill55
File created: October 12, 2024
******************************
this file is the file used check how many groups of characters there are in the password. there are 4 groups, uppercase, lowercase, digits, and symbols. the more groups, the stronger the password. then in the second function in this file, the strength is calculated by looking at the length of the password and the amount of groups.
"""


# this function will be used to figure out how strong the password is
def count_groups(pwd):
    # these are the differnt kinds of groups (lowercase, uppercase, digits, symbols)the password can contain
    lowercase = set("abcdefghijklmnopqrstuvwxyz")
    uppercase = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    digits = set("0123456789")
    symbols = set("!@#$%^&*/?-+=,.|~")

    # these are basicly booleen values to tell me if there is a lowercase, upercase etc. The reason i didnt use booleen values was because i wanted to add up all the values togather after to see how many groups were there
    lowercase_count = 0
    uppercase_count = 0
    digits_count = 0
    symbols_count = 0
    count = 0  # this will be the total number of groups used

    # loop through each character in the password and see if it belongs to any group
    for char in pwd:
        if char in lowercase:
            lowercase_count = 1
        elif char in uppercase:
            uppercase_count = 1
        elif char in digits:
            digits_count = 1
        elif char in symbols:
            symbols_count = 1

    # this will tell us how many groups there are in the password
    count = lowercase_count + uppercase_count + digits_count + symbols_count

    return count  # return the number of groups


# this function will calculate the strength of the password
def password_strength(pwd):
    # we want to check if the password has any invalud characters
    if ' ' in pwd or '\t' in pwd or '\n' in pwd:
        return 0  # if it does, return 0 because the password is weak

    # get the length of the password
    length = len(pwd)

    # we have to find out how many groups there are in the password, so we call the function
    num_groups = count_groups(pwd)

    # now we check the strength  of the password
    if length < 5:
        return 0  # too short, return 0 strength
    elif 5 <= length <= 8:
        if num_groups == 0 or num_groups == 1:
            return 1  # very weak
        elif 2 <= num_groups <= 3:
            return 2  # medium strength
        elif num_groups == 4:
            return 3  # strong
    elif 9 <= length <= 12:
        if num_groups == 0 or num_groups == 1:
            return 2  # weak for this length
        elif 2 <= num_groups <= 3:
            return 3  # stronger
        elif num_groups == 4:
            return 4  # very strong
    elif length > 12:
        if num_groups == 0 or num_groups == 1:
            return 3  # still weak despite long length
        elif 2 <= num_groups <= 3:
            return 4  # stronger but not the best
        elif num_groups == 4:
            return 5  # maximum strength

    return 0  # just a fallback in case something unexpected happens (shouldn't happen though)
