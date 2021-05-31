""" Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr.Abi Evans and Andrew Jelani
Home work 4
Problem 1:palindrome.py
Program description: This program checks if a supplied string is a palindrome
or not.
"""


import string


def is_palindrome(words):
    '''
    Function -- is_palindrome
        Check if a string is plindrome or not.
    Parameters:
        words -- A string that needs to be checked palindrome.
    Returns:
        Boolean retur. If the string is palindrome, return ture. Otherwise,
        false.
    '''

    if is_str(words):
        temp_words = remove_space(words)
        if len(temp_words) >= 2:
            lower_words = temp_words.lower()
            value = True
            i = 1
            while value and i <= len(lower_words):
                if lower_words[i-1] != lower_words[-i]:
                    value = False
                i += 1
            return value
    return False


def is_str(words):
    '''
     Function -- is_str
        Check if words are string type.
     Parameters:
        words -- A string to be checked string type or not.
     Returns:
        Boolean reture. If the words are string, return true. Otherwise, false.
    '''

    return isinstance(words, str)


def remove_space(words):
    '''
    Function -- remove_space
        Remove spaces in words.
    Parameters:
        words -- A string to be reomved space.
    Returns:
    The new words without space in it.
    '''

    return words.replace(" ", "")


def main():
    print(remove_space("dog  dog dog"))
    print(is_str("words"))
    print(is_palindrome("madam Im adam"))
    print(is_palindrome("a"))
    print(is_palindrome("RADar"))
    print(is_palindrome("!RADar!"))


if __name__ == "__main__":
    main()
