from problem_3 import (weekday_num, num_day_until)
import pytest


def test_num_day_until():
    assert (num_day_until(1, 4) == 3)
    assert (num_day_until(1, 6) == 5)
    assert (num_day_until(5, 1) == 3)


def test_weekday_num():
    assert (weekday_num("M") == 1)
    assert (weekday_num("TU") == 2)
    assert (weekday_num("F") == 5)
