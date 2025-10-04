# tests/test_integration.py
from validate import validate_items
from calc import compute_total

def test_validate_then_compute():
    items = [{'name':'A','qty':2,'price':2.5}, {'name':'B','qty':1,'price':5.0}]
    assert validate_items(items) is True
    # Si la validación pasa, podemos confiar en que compute_total funciona sobre datos válidos
    assert compute_total(items) == 10.0
