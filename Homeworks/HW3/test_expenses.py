from expenses import (calculate_mileage, get_reimbursement_amount,
                      get_actual_mileage_rate, get_actual_trip_cost)


def test_calculate_mileage():
    assert(calculate_mileage(10, 10) == 0)
    assert(calculate_mileage(30, 100) == 70)
    assert(calculate_mileage(100, 30) == 0)


def test_get_reimbursement_amount():
    assert(get_reimbursement_amount(10) == 5.75)
    assert(get_reimbursement_amount(0) == 0)


def test_get_actual_mileage_rate():
    assert(get_actual_mileage_rate(0, -1) == 0)
    assert(get_actual_mileage_rate(-15, -15) == 0)


def test_get_actual_trip_cost():
    assert(get_actual_trip_cost(0, -1, 0, -1) == 0)
    assert(get_actual_trip_cost(47001, 48001, 24, 2.00) == 83.33)
