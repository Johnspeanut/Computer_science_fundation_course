""" Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr.Abi Evans and Andrew Jelani
Home work 5
Problem 2:password.py
Program description: Take a string and check if it is a secure password
according to some rules.
"""


import string


def least_one_upper(str_input):
    '''
    Function -- least_one_upper
    Check if there is at least one upper case
    Parameter:
    str_input-- string input
    Return -- int, length of a string
    '''

    return any(x.isupper() for x in str_input)


def least_one_lower(str_input):
    '''
    Function -- least_one_lower
    Check if there is at least one lower case
    Parameter:
    str_input-- string input
    Return -- int, length of a string
    '''

    return any(x.islower() for x in str_input)


def least_one_digit(str_input):
    '''
    Function -- least_one_digit
    Check if there is at least one digit
    Parameter:
    str_input-- string input
    Return -- int, length of a string
    '''

    return any(x.isdigit() for x in str_input)


def least_one_special(str_input):
    '''
    Function -- east_one_special
    Check if there is at least one special of four $, #, !, and @
    Parameter:
    str_input-- string input
    Return -- int, length of a string
    '''
    isSpecial = False
    for i in range(len(str_input)):
        if str_input[i] in ["$", "#", "!", "@"]:
            isSpecial = True
    return isSpecial


def no_other_special(str_input):
    '''
    Function -- no_other_special
    Check if there is no other special than $, #, !, and @
    Parameter:
    str_input-- string input
    Return -- True if no other special than $, #, !, and @
    '''

    list_of_lists = [list(string.ascii_lowercase),
                     list(string.ascii_uppercase),
                     list(string.digits), "$", "#", "!", "@"]
    flattened_list = [val for sublist in list_of_lists for val in sublist]
    return all((x in flattened_list) for x in list(str_input))


def secure_password(str_input):
    '''
    Function -- secure_password
    Check if a string is a valid password
    Parameter:
    str_input-- string of password
    Return -- Return true if valid. Otherwise, false.
    '''

    if len(str_input) >= 9 and len(str_input) <= 12 and\
       no_other_special(str_input):
        if least_one_upper(str_input) + least_one_lower(str_input) +\
           least_one_digit(str_input) + least_one_special(str_input) >= 3:
            return True
    return False
