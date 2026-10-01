def web_total(items):
    """Same invoice pricing rule as batch_total."""
    subtotal = sum(price * quantity for price, quantity in items)
    tax = subtotal * 0.17
    return subtotal + tax

def batch_total(items):
    subtotal = sum(price * quantity for price, quantity in items)
    tax = subtotal * 0.17
    return subtotal + tax
