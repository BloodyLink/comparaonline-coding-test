import pytest

from after_30_days import car_insurance_prices

def test_after_30_days():
    car_insurance_prices()
    with open('products_after_30_days.txt', 'r') as result, open('tests/expected_result.txt', 'r') as expected:
        assert result.read() == expected.read()
