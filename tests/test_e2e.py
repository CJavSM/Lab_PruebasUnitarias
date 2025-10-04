# tests/test_e2e.py
from action import place_order

def test_e2e_default_gateway():
    items = [
        {'name':'A','qty':1,'price':5.00},
        {'name':'B','qty':3,'price':2.00}
    ]
    # Usamos payment_gateway=None => usa el simulacro interno (ok)
    order = place_order(items, discount_percent=5, payment_gateway=None)
    assert order['status'] == 'placed'
    assert order['total'] == 11.0  # 5 + (3*2) = 11
    assert order['final_total'] == 10.45  # 11 - 5% = 10.45
    assert order['payment']['ok'] is True
