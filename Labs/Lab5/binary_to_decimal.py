""" Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr.Abi Evans and Andrew Jelani
Lab 5
Problem 2:binary to decimal
"""


def reverse_str(string_input):
    '''
    Function -- reverse_str
    Reverse a string
    Parameter:
    string_input -- A string to be reversed
    Return -- A reversed string
    '''
    rever_string = ""
    for i in range(len(string_input) - 1, -1, -1):
        rever_string += string_input[i]
    return rever_string


def binary_to_decimal(binary_num_str):
    '''
    Function -- binary_to_decimal
    Reverse a string
    Parameter:
    binary_num_str -- A string with binary number
    Return -- Integer data type and demical.
    '''

    reversed_str = reverse_str(binary_num_str)
    total = 0
    for i in range(len(reversed_str)):
        total += int(reversed_str[i]) * (2 ** i)
    return total


def main():
    bi_value = input("Enter a binary number to be converted to decimal: ")
    decimal_value = binary_to_decimal(bi_value)
    print("The binary {} can be converted to decimal with value of {}".format(
          bi_value, decimal_value))


if __name__ == "__main__":
    main()
