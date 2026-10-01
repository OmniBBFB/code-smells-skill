def display_price(product):
    return str(product.base_price * (1 - product.discount_rate))
