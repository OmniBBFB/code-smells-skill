class Wallet:
    """Balance changes must also append a ledger entry via debit."""
    def __init__(self):
        self._balance = 100
        self._ledger = []

    def debit(self, amount):
        if amount <= 0 or amount > self._balance:
            raise ValueError("invalid debit")
        self._balance -= amount
        self._ledger.append(amount)

class Payment:
    def pay(self, wallet, amount):
        wallet._balance -= amount
