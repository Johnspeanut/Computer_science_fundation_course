""" Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr.Abi Evans and Andrew Jelani
Lab 5
Problem 1:Scores
"""


def average(num_list):
    '''
    Function -- average
        Calculate average of elements of a list
    Parameters:
        num_list -- A list of numbers
    Returns:
        float data type. Average of elements of the list.
    '''
    total = 0.0
    for i in range(len(num_list)):
        total += num_list[i]
    return total / len(num_list)


def sort_order(num_list_origial):
    '''
    Function -- sort_order
        sort a order of a number list
    Parameters:
        num_list_origial -- A list of numbers
    Returns:
        A list with increasing order
    '''
    num_list = num_list_origial
    for i in range(len(num_list)):
        for j in range(len(num_list) - 1):
            if num_list[j] > num_list[j+1]:
                temp = num_list[j]
                num_list[j] = num_list[j+1]
                num_list[j+1] = temp
    return num_list


def median(num_list_origial):
    '''
    Function -- median
        Calculate the median of elements of a list
    Parameters:
        num_list_origial -- A list of numbers
    Returns:
        float data type. Median of the elements of the list
    '''
    num_list = sort_order(num_list_origial)
    if len(num_list) % 2 == 0:
        median_value = (num_list[len(num_list) // 2 - 1] +
                        num_list[len(num_list) // 2 ]) / 2 
    else:
        median_value = num_list[len(num_list) // 2]
    return median_value


def lowest(num_list):
    '''
    Function -- lowest
        Find the lowest value of elements in list
    Parameters:
        num_list -- A list of numbers
    Returns:
        Lowest number
    '''
    temp_list = sort_order(num_list)
    return temp_list[0]


def highest(num_list):
    '''
    Function -- highest
        Find the highest value of elements in list
    Parameters:
        num_list -- A list of numbers
    Returns:
        Highest number
    '''
    temp_list = sort_order(num_list)
    return temp_list[len(temp_list) - 1]
