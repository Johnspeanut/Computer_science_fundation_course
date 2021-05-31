from problem_1 import (downpayment, save_monthly, months_need_for_downpayment,
                        years_need_for_save, months_need_for_save)
import pytest


def test_downpayment():
    assert pytest.approx(downpayment(700000, 0.4) == 280000)
    assert pytest.approx(downpayment(500000, 0.4) == 200000)
    assert pytest.approx(downpayment(1000000, 0.5) == 500000)


def test_save_monthly():
    assert pytest.approx(save_monthly(5000, 0.3) == 1500)
    assert pytest.approx(downpayment(1000, 0.4) == 400)
    assert pytest.approx(downpayment(2000, 0.5) == 1000)


def test_months_need_for_downpayment():
    assert pytest.approx(months_need_for_downpayment(0, 0) == 0)


def test_years_need_for_save():
    assert pytest.approx(years_need_for_save(22500) == 1)


def test_months_need_for_save():
    assert pytest.approx(months_need_for_save(22500) == 10)
