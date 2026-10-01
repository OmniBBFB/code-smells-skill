def f(x):
    # x is the amount in cents. A customer gets a discount only above 10000.
    # y is the discounted amount. The multiplier 0.9 is the premium discount.
    # z is the shipping fee. Shipping is free for qualifying large purchases.
    if x > 10000:
        y = x * 0.9
        z = 0
    else:
        y = x
        z = 500
    return y + z
