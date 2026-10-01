class Ledger:
    """All operations preserve the same append-only account history."""
    def __init__(self):
        self.entries = []

    def record(self, amount):
        self.entries.append(amount)

    def balance(self):
        return sum(self.entries)

    def last_entry(self):
        return self.entries[-1]
