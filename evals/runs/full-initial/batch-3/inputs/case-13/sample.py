def shipping(total):
    return 0 if total >= 100 else 10

def cart(total):
    return shipping(total)

def checkout(total):
    return shipping(total)
