# tests/test_calc.py
import pytest
from calc import compute_total, apply_discount

def test_compute_total_basic():
    items = [{'name':'A','qty':2,'price':3.5}, {'name':'B','qty':1,'price':1.0}]
    assert compute_total(items) == 8.0

@pytest.mark.parametrize("items, expected", [
    ([], 0.0),
    ([{'name':'x','qty':0,'price':100}], 0.0),
    ([{'name':'y','qty':3,'price':0}], 0.0),
])
def test_compute_total_edgecases(items, expected):
    assert compute_total(items) == expected

def test_apply_discount_normal():
    assert apply_discount(100.0, 10) == 90.0

def test_apply_discount_bounds():
    assert apply_discount(50.0, 0) == 50.0
    assert apply_discount(50.0, 100) == 0.0

def test_apply_discount_invalid():
    with pytest.raises(ValueError):
        apply_discount(100, -1)
    with pytest.raises(ValueError):
        apply_discount(100, 105)
