# action.py
import calc
import validate
from typing import List, Dict, Callable, Optional

def place_order(
    items: List[Dict],
    discount_percent: float = 0.0,
    payment_gateway: Optional[Callable[[float], Dict]] = None
) -> Dict:
    """Flujo: validar -> calcular total -> aplicar descuento -> procesar pago.
    payment_gateway es una función inyectable que recibe el monto y devuelve dict {'ok': bool, ...}
    Si payment_gateway es None se usa un simulacro local (fake).
    """
    # 1) Validar
    validate.validate_items(items)

    # 2) Calcular
    total = calc.compute_total(items)
    final_total = calc.apply_discount(total, discount_percent)

    # 3) Pagar (simulado o inyectado)
    if payment_gateway is None:
        # simulacro sencillo
        payment_result = {'ok': True, 'tx_id': 'fake_tx_1', 'amount': final_total}
    else:
        payment_result = payment_gateway(final_total)

    if not payment_result.get('ok', False):
        raise RuntimeError("Pago fallido")

    # retorno simple con info del pedido
    return {
        'status': 'placed',
        'total': total,
        'final_total': final_total,
        'items': items,
        'payment': payment_result
    }
