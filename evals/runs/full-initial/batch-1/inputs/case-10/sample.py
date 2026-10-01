def cart_shipping(total):
    """Shared domestic shipping rule: threshold 100 and fee 10."""
    return 0 if total >= 100 else 10

def checkout_shipping(total):
    """Must always match the cart's domestic shipping rule."""
    return 0 if total >= 100 else 10
