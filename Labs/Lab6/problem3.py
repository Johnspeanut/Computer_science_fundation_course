""" Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr.Abi Evans and Andrew Jelani
Lab 6
Problem 3:More recursion practice
"""


def log_2(num):
    '''
    Function -- log_2
    # Logarithm using recursive function
    Parameter:
    num -- integer number
    Output -- logorithm value
    '''

    if num / 2 == 1:
        return 1
    else:
        return 1 + log_2(num / 2)


# print(log_2(2))
# print(log_2(8))
# print(log_2(16))
# print(log_2(32))
# print(log_2(64))


def base2_to_normal(str_base_2_num):  #binary to decimal
    '''
    Function -- base2_to_normal
    Calculate equivalent normal number based on a number with base 2.
    Parameter:
    str_base_2_num -- a base-2 number with string data type
    Output -- integer num with normal base
    '''

    if len(str_base_2_num) == 1:
        return int(str_base_2_num[0])
    else:
        return int(str_base_2_num[0]) * 2 ** len(str_base_2_num[1:]) + base2_to_normal(str_base_2_num[1:])


print(base2_to_normal("1101"))
print(base2_to_normal("1111101"))
print(base2_to_normal("11110100"))
print(base2_to_normal("11001"))
