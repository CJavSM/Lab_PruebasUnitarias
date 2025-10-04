# tests/test_action.py
import pytest
from action import place_order

def test_place_order_success_with_injected_gateway():
    items = [{'name':'A','qty':2,'price':10.0}]
    def fake_payment(amount):
        return {'ok': True, 'tx_id': 'tx123', 'amount': amount}
    order = place_order(items, discount_percent=10, payment_gateway=fake_payment)
    assert order['status'] == 'placed'
    assert order['final_total'] == 18.0  # 20 - 10% = 18
    assert order['payment']['ok'] is True

def test_place_order_payment_fail():
    items = [{'name':'A','qty':1,'price':1.0}]
    def fail_payment(amount):
        return {'ok': False}
    with pytest.raises(RuntimeError):
        place_order(items, payment_gateway=fail_payment)
