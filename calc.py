# calc.py
from typing import List, Dict

def compute_total(items: List[Dict]) -> float:
    """Suma qty * price por cada item. Redondea a 2 decimales."""
    total = 0.0
    for it in items:
        total += float(it['qty']) * float(it['price'])
    return round(total, 2)

def apply_discount(total: float, percent: float) -> float:
    """Aplica un descuento porcentual. percent en [0,100]."""
    if not (0 <= percent <= 100):
        raise ValueError("percent debe estar entre 0 y 100")
    return round(total * (1 - percent / 100.0), 2)
