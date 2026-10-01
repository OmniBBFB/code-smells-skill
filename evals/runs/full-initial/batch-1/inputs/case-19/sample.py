class Invoice:
    def __init__(self, amount):
        self.amount = amount

    def total_with_tax(self):
        return self.amount * 1.17

    def html(self):
        return "<section class='invoice'>" + str(self.amount) + "</section>"

    def save(self, db):
        db.execute("INSERT INTO invoices(amount) VALUES (?)", (self.amount,))
