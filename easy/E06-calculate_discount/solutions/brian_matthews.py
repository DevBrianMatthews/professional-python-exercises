
def calculate_discount(price: float, discount: float, tax: float = 0.0) -> dict:

    if price <= 0:
        raise ValueError('price must be greater than 0')
    if not 0 <= discount <= 100:
        raise ValueError('discount must be between 0 and 100')
    if not 0 <= tax <= 100:
        raise ValueError('tax must be between 0 and 100')

    discount_amount = (price * discount) / 100
    discount_price  = price - discount_amount
    tax_amount      = (discount_price * tax) / 100
    final_price     = discount_price + tax_amount

    return {
        'original_price':  round(price, 2),
        'discount_amount': round(discount_amount, 2),
        'tax_amount':      round(tax_amount, 2),
        'final_price':     round(final_price, 2)
        }

print(calculate_discount(100.0, 20.0, 19.0))
