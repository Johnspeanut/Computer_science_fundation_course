""" Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr.Abi Evans and Andrew Jelani
Home work 5
Problem 2:upc.py
Program description: The program is to determine whether a number is a valid
Universal Product Code(UPC).
"""


import string


def isNum(str_num):
    '''
    Function -- isNum
    Check if a string is only consisted of number
    Parameter:
    str_num-- String type. A number to be listed.
    Return -- If every character is number, return true
    '''

    return all((x in list(string.digits)) for x in list(str_num))


def reverse_list(list_num):
    '''
    Function -- reverse_list
    Reverse a list
    Parameter:
    list_num-- A list
    Return -- A reversed list
    '''
    rever_list = []
    for i in range(len(list_num) - 1, -1, -1):
        rever_list.append(list_num[i])
    return rever_list


def char_to_num(list_num):
    '''
    Function -- char_to_num
    Change a list of char to a list of integer
    Parameter:
    list_num-- A list of char
    Return -- A list of integer
    '''
    new_list = []
    for i in range(len(list_num)):
        new_list.append(int(list_num[i]))
    return new_list


def is_valid_upc(product_code):
    '''
    Function -- is_valid_upc
    Check if a upc is valid or not
    Parameter:
    product_code-- string of code
    Return -- Return true if valid. Otherwise, false.
    '''

    if isNum(product_code) and len(product_code) != 0:
        num_list = list(product_code)
        left_right_list = reverse_list(num_list)
        correct_list_num = char_to_num(left_right_list)
        sum = 0
        for i in range(len(correct_list_num)):
            if i % 2 != 0:
                correct_list_num[i] = correct_list_num[i] * 3
            sum += correct_list_num[i]
        if sum % 10 == 0:
            return True
    return False
