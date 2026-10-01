import csv

class Account:
    """Public read-only reporting projection, not the write model."""
    def __init__(self, name, balance, currency):
        self.name = name
        self.balance = balance
        self.currency = currency

class AccountReport:
    def export(self, accounts, stream):
        writer = csv.writer(stream)
        for account in accounts:
            writer.writerow([account.name, account.balance, account.currency])
