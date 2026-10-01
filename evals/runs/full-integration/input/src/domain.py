from dataclasses import dataclass


@dataclass(frozen=True)
class OrderPayload:
    """Transport DTO; business validation belongs to the domain services."""
    total: int


class Wallet:
    """debit must atomically keep balance changes and ledger entries together."""
    def __init__(self, balance):
        self._balance = balance
        self._ledger = []

    def debit(self, amount):
        if amount <= 0 or amount > self._balance:
            raise ValueError("invalid debit")
        self._balance -= amount
        self._ledger.append(amount)
