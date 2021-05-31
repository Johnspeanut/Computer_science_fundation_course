""" Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr.Abi Evans and Andrew Jelani
Home work 4
Problem 2:hangman.py
Program description: This program is to implement a Hangman game. In the game,
player has six guesses. If the guesses match secret words, he(she) wins.
"""


import string


def underscore_replace(words):
    '''
    Function -- underscore_replace
        Replace characters with underscores.
    Parameters:
        words -- A string that needs to be replaced.
    Returns:
        underscore string
    '''

    return "_" * len(words)


def letter_in_word(letter, word):
    '''
    Function -- letter_in_word
        Check a letter in a word.
    Parameters:
        letter -- A letter to be checked.
        words -- A string.
    Returns:
        True if letter in a word. Otherwise, false.
    '''
    i = 0
    value = False
    while i < len(word):
        if word.upper()[i] == letter.upper():
            value = True
        i += 1
    return value


def replace_underscore_with_letter(secret_word, underscore_character, letter):
    '''
    Function -- replace_underscore_with_letter
        replace underscore symbol with letter
    Parameters:
        secret_word -- Select word.
        underscore_character -- "_" with number of length of secret_word
        letter -- A letter being checked
    Returns:
        String with showing letter. Others are underscore.
    '''

    i = 0
    new_word = ""
    while i < len(secret_word):
        if secret_word[i] == letter:
            value = letter
        else:
            value = underscore_character[i]
        new_word += value
        i += 1
    return new_word


def isWin(input_word, secret_word):
    '''
    Function -- isWin
        Check if win condition meet
    Parameters:
        secret_word -- expected word.
        input_word -- word to be checked.
    Returns:
        Boolean. If win, return True. Otherwise, false.
    '''
    if input_word.upper() == secret_word:
        return True
    else:
        return False


def main():
    count_win = 0
    for words in ["APPLE", "OBVIOUS", "XYLOPHONE"]:
        underscore_character = underscore_replace(words)
        print(underscore_character)
        i = 0
        guessed_letter = ""
        win = False
        while i < 6 and (not win):
            letter = input("Enter a letter or word: ").upper()
            if isWin(underscore_character, words) or isWin(letter, words):
                win = True
            elif len(letter) == 1:
                if letter_in_word(letter, guessed_letter):
                    print("You've already guessed that letter!")
                elif letter == "":
                    underscore_character = underscore_character
                    guessed_letter = guessed_letter
                else:
                    guessed_letter += letter
                    if letter_in_word(letter, words):
                        underscore_character = replace_underscore_with_letter(
                            words, underscore_character, letter)
                    i += 1
                if i == 6:
                    break
                print(underscore_character)
                print("Your guesses so far:", guessed_letter)
        if win:
            print("You win!")
            count_win += 1
        else:
            print("You lose! The word was", words)
    print("You won {} out of 3".format(count_win))


if __name__ == "__main__":
    main()