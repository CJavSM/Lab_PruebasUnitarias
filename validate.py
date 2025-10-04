# validate.py
from typing import List, Dict

def validate_items(items: List[Dict]) -> bool:
    """Valida formato y valores mínimos de una lista de items.
    Cada item debe tener 'name', 'qty' (int >=0) y 'price' (>=0).
    """
    if not isinstance(items, list):
        raise TypeError("items debe ser una lista")

    for i, it in enumerate(items):
        if not isinstance(it, dict):
            raise ValueError(f"item {i} debe ser un dict")
        for key in ('name', 'qty', 'price'):
            if key not in it:
                raise ValueError(f"Falta clave '{key}' en item {i}")
        qty = it['qty']
        price = it['price']
        if not (isinstance(qty, int) and qty >= 0):
            raise ValueError(f"qty inválido en item {i}")
        if not (isinstance(price, (int, float)) and price >= 0):
            raise ValueError(f"price inválido en item {i}")
    return True
