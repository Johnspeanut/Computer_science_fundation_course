""" Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr.Abi Evans and Andrew Jelani
Home work 4
Problem 2:hangman.py
"""

def underscore_all_letter(secret_word):
    '''
    Function -- underscore_all_letter
        underscore all letters
    Parameters:
        secret_word -- A string.
    Returns:
        underscores with length of secrete words
    '''
    return "_" * len(secret_word)

def check_letter_in_secrete(guess, secrete_word):
    '''
    Function -- check_letter_in_secrete
        underscore all letters
    Parameters:
        secret_word -- A string.
    Returns:
        True if letter in a word. Otherwise, false.
    '''
    i = 0
    value = False
    while i < len(guess):
        if secrete_word[i] == guess:
            value = True
        i += 1
    return value

def store_guess_word(guess, word):
    '''
    Function -- store_guess_word
        store guess word
    Parameters:
        guess -- A string.
        word -- The guess word based on
    Returns:
        word
    '''
    if check_letter_in_secrete(guess, word):
        return word
    else:
        return word + guess

def guess_result(guess, current_underscore, secret_word):
    if check_letter_in_secrete(guess, secrete_word) and not check_letter_in_secrete(guess, current_underscore):
        return 





def main():
    count_win = 0
    for words in ["APPLE", "OBVIOUS", "XYLOPHONE"]:
        print(underscore_all_letter(words))
        i = 0
        win = False
        while i < 6 and not win:
            guess = input("Enter a letter or word: ")
            store_word = ""
            if len(guess) > 1:
                if guess == words:
                    win = True
            else:
                if check_letter_in_secrete(guess, store_word):
                    print("You've already guessed that letter!")
                elif check_letter_in_secrete(guess, words):
                    store_word = store_guess_word(guess, store_word)
                    i += 1
                    if check_secrete_word(guess, words) == words:
                        win = True
                else:
                    i += 1
            print()
            print("Your guesses so far: ")
        if win:
            count_win += 1
        else:
            print("You lsoe! The word was ", words)
    print("You won {} out of 3".format(count_win))





if __name__ == "__main__":
    main()