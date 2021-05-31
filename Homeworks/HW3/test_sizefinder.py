from sizefinder import size_checker


def test_size_checker():
    assert(size_checker(27, "K") == "S")
    assert(size_checker(28, "K") == "M")
    assert(size_checker(0, "K") == "not available")
    assert(size_checker(30, "W") == "S")
    assert(size_checker(40, "W") == "XXXL")
    assert(size_checker(0, "W") == "not available")
    assert(size_checker(34, "M") == "S")
    assert(size_checker(0, "M") == "not available")
    assert(size_checker(50, "M") == "XXXL")
