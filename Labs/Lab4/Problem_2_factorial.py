""" Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr.Abi Evans and Andrew Jelani
Lab 4
Problem 2:Factorial
"""


def factorial(number):
    '''
    Function -- factorial
        Calculate factorial value.
    Parameters:
        number -- Integer number to be factorized.
    Returns:
        return integer value
    '''
    value = 1
    i = 1
    while i <= number:
        value *= i
        i += 1
    return value


def main():
    number = int(input("Enter a positive integer: "))
    print(factorial(number))


if __name__ == "__main__":
    main()
