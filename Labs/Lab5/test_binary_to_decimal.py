from binary_to_decimal import reverse_str, binary_to_decimal


def test_reverse_str():
    assert(reverse_str("string_input") == "tupni_gnirts")
    assert(reverse_str("doog") == "good")
    assert(reverse_str("love") == "evol")

