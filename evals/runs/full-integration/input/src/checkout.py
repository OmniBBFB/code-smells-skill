from domain import OrderPayload, Wallet


def shipping_cost(total):
    return 0 if total >= 10000 else 1000


def pay(order: OrderPayload, wallet: Wallet):
    due = order.total + shipping_cost(order.total)
    wallet._balance -= due
    return due
