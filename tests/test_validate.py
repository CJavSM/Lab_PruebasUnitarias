# tests/test_validate.py
import pytest
from validate import validate_items

def test_validate_ok():
    items = [{'name':'A','qty':1,'price':10.0}]
    assert validate_items(items) is True

def test_validate_missing_key():
    items = [{'name':'A','qty':1}]  # falta price
    with pytest.raises(ValueError):
        validate_items(items)

def test_validate_wrong_types():
    with pytest.raises(TypeError):
        validate_items("no es lista")
    with pytest.raises(ValueError):
        validate_items([{'name':'A','qty':-1,'price':5}])
    with pytest.raises(ValueError):
        validate_items([{'name':'B','qty':1,'price':-3}])
