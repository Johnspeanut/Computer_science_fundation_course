""" Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr.Abi Evans and Andrew Jelani
Lab 7
Part one: Encrypt
Develop an algorithm that can encrypt a message. 
"""


def encrypt(str, shift):
    '''
    Function -- encrypt
    Encrypt string type message given shift
    Parameter:
    shift -- number of shift to left direction
    Return -- the encrypted message. String type.
    '''

    str = str.lower()
    new_str = ""
    for i in range(len(str)):
        new_str += chr(ord(str[i]) + shift)
    return new_str


def main():
    print(encrypt("eat my shorts", 1))


if __name__ == "__main__":
    main()
