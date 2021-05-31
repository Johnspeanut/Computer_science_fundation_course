from scores import average, sort_order, median, lowest, highest


num_list_1 = [5, 9, 4, 1, 0]
num_list_2 = [0, 0, 0, 0, 0, 0, 0, 0]
num_list_3 = [-2, -2, -2, -2, -2, -2, -2, -2, -2]
num_list_4 = [-1, -1, -1, 1, 1, 1]
num_list_5 = [5, 9, 4, 1, 0, 45, 67, 12, -45]


def test_average():
    assert(average(num_list_2) == 0)
    assert(average(num_list_3) == -2)
    assert(average(num_list_4) == 0)


def test_sort_order():
    assert(sort_order(num_list_1) == [0, 1, 4, 5, 9])


def test_median():
    assert(median(num_list_1) == 4)
    assert(median(num_list_2) == 0)
    assert(median(num_list_3) == -2)


def test_lowest():
    assert(lowest(num_list_1) == 0)
    assert(lowest(num_list_5) == -45)
    assert(lowest(num_list_4) == -1)


def test_highest():
    assert(highest(num_list_1) == 9)
    assert(highest(num_list_4) == 1)
    assert(highest(num_list_5) == 67)
