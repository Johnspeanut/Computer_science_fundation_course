from hangman import (underscore_replace, letter_in_word,
                     replace_underscore_with_letter, isWin)


def test_underscore_replace():
    assert(underscore_replace("madam") == "_____")
    assert(underscore_replace("a") == "_")
    assert(underscore_replace("b b") == "___")


def test_letter_in_word():
    assert(letter_in_word("c", "Cat") is True)
    assert(letter_in_word("d", "cat") is False)
    assert(letter_in_word("j", "John") is True)


def test_replace_underscore_with_letter():
    assert(replace_underscore_with_letter("dog", "___", "d") == "d__")
    assert(replace_underscore_with_letter("zoom", "____", "o") == "_oo_")
    assert(replace_underscore_with_letter("tree", "____", "e") == "__ee")


def test_isWin():
    assert(isWin("dog", "dog") is True)
    assert(isWin("cat", "dog") is False)
    assert(isWin("car", "car") is True)
