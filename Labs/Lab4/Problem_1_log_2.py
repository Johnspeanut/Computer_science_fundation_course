""" Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr.Abi Evans and Andrew Jelani
Lab 4
Problem 1:Logarithm
"""


def log_2(number):
    '''
    Function -- log_2
        Calculate log with base 2.
    Parameters:
        number -- Integer number to be logarithm.
    Returns:
        return integer value
    '''
    count =0
    while number / 2 >= 1:
        number = number / 2
        count += 1
    return count

def log(base, number):
    '''
    Function -- log
        Calculate log with base .
    Parameters:
        base -- base.
        number -- Integer number to be logarithm.
    Returns:
        return integer value
    '''
    count =0
    while number / base >= 1:
        number = number / base
        count += 1
    return count


def main():
    number = int(input("Enter a positive integer: "))
    print(log_2(number))
    print(log(3, number))
    print(log(10, number))

if __name__ == "__main__":
    main()
