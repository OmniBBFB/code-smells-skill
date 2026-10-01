class BusinessDesk:
    def __init__(self, db, printer, cron):
        self.db = db
        self.printer = printer
        self.cron = cron
        self.staff = {}

    def calculate_tax(self, amount):
        return amount * 0.17

    def persist_invoice(self, invoice):
        statement = "INSERT INTO invoices VALUES (?, ?)"
        self.db.execute(statement, (invoice["id"], invoice["amount"]))

    def print_badge(self, employee_id):
        self.printer.print_text("Badge: " + self.staff[employee_id])

    def add_night_shift(self, employee_id, date):
        self.cron.add(date, employee_id)

    def hire(self, employee_id, name):
        self.staff[employee_id] = name
