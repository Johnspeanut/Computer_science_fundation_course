from palindrome import is_palindrome, is_str, remove_space


def test_is_palindrome():
    assert(is_palindrome("madam Im adam") is True)
    assert(is_palindrome("a") is False)
    assert(is_palindrome("b") is False)
    assert(is_palindrome(12321) is False)
    assert(is_palindrome("RA  Dar") is True)
    assert(is_palindrome("!RADar!") is True)
    assert(is_palindrome("_") is False)
    assert(is_palindrome(" a") is False)


def test_is_str():
    assert(is_str(30) is False)
    assert(is_str("sdslf") is True)
    assert(is_str("1232") is True)


def test_remove_space():
    assert(remove_space("dog dog dog") == "dogdogdog")
    assert(remove_space("d o g") == "dog")
    assert(remove_space("C a T") == "CaT")
