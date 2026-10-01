class CreditAccount:
    """Domain write model; spent must remain within limit."""
    def __init__(self, limit):
        self.limit = limit
        self.spent = 0

def purchase(account, amount):
    if amount > 0 and account.spent + amount <= account.limit:
        account.spent += amount
        return True
    return False

def reserve(account, amount):
    if amount > 0 and account.spent + amount <= account.limit:
        account.spent += amount
        return True
    return False
