from upc import isNum, reverse_list, char_to_num, is_valid_upc


def test_isNum():
    assert(isNum("123") is True)
    assert(isNum("abc") is False)
    assert(isNum("dog") is False)


def test_reverse_list():
    assert(reverse_list([1, 2, 3]) == [3, 2, 1])
    assert(reverse_list(["a", "b", "c"]) == ["c", "b", "a"])
    assert(reverse_list(["a", "b", "c"]) != ["b", "b", "a"])


def test_char_to_num():
    assert(char_to_num(["1", "2", "3"]) == [1, 2, 3])
    assert(char_to_num(["1", "5", "6"]) == [1, 5, 6])
    assert(char_to_num(["8", "9", "0"]) == [8, 9, 0])


def test_is_valid_upc():
    assert(is_valid_upc("9780128053904") is True)
    assert(is_valid_upc("9780128055904") is False)
