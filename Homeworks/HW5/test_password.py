from password import (least_one_upper, least_one_lower, least_one_digit,
                      least_one_special, no_other_special, secure_password)


def test_least_one_upper():
    assert(least_one_upper("Jadf12") is True)
    assert(least_one_upper("123456a") is False)
    assert(least_one_upper("AAAEEE") is True)


def test_least_one_lower():
    assert(least_one_lower("Jadf12") is True)
    assert(least_one_lower("123456A") is False)
    assert(least_one_lower("AAAEEE@") is False)


def test_least_one_digit():
    assert(least_one_digit("Jadf12") is True)
    assert(least_one_digit("JadfDD") is False)
    assert(least_one_digit("Jadf1@!") is True)


def test_least_one_special():
    assert(least_one_special("Jadf12") is False)
    assert(least_one_special("Jadf1@") is True)
    assert(least_one_special("Jadf1!") is True)


def test_no_other_special():
    assert(no_other_special("Jadf12@") is True)
    assert(no_other_special("Jadf1$#") is True)
    assert(no_other_special("Jadf1290*") is False)


def test_secure_password():
    assert(secure_password("Jadfdfd12@") is True)
    assert(secure_password("JaJJKdfd1##") is True)
    assert(secure_password("JaJJKdfd1") is True)
