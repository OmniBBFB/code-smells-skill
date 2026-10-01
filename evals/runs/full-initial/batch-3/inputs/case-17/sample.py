def close_day(records, db, mailer, storage):
    """Single daily closure entry; effects have independent failure policies."""
    accepted = []
    rejected = []
    for row in records:
        if row["amount"] < 0:
            rejected.append(row)
        elif not row["customer"]:
            rejected.append(row)
        else:
            accepted.append(row)
    totals = {}
    for row in accepted:
        customer = row["customer"]
        totals[customer] = totals.get(customer, 0) + row["amount"]
    invoice_rows = []
    for customer, total in totals.items():
        tax = total * 0.1
        invoice_rows.append((customer, total, tax))
    db.begin()
    try:
        for customer, total, tax in invoice_rows:
            db.insert_invoice(customer, total, tax)
        db.commit()
    except Exception:
        db.rollback()
        raise
    page = "<table>"
    for customer, total, tax in invoice_rows:
        page += f"<tr><td>{customer}</td><td>{total + tax}</td></tr>"
    page += "</table>"
    storage.write("daily.html", page)
    for customer, total, tax in invoice_rows:
        mailer.send(customer, f"Due {total + tax}")
    return rejected
