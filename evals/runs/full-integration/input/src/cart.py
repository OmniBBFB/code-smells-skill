from domain import OrderPayload


def shipping_cost(total):
    return 0 if total >= 10000 else 1000


def preview(order: OrderPayload):
    return order.total + shipping_cost(order.total)
