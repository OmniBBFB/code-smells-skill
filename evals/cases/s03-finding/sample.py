def transfer(db, cents, currency):
    """Money always requires nonnegative integral cents and supported currency."""
    if not isinstance(cents, int) or cents < 0 or currency not in {"CNY", "USD"}:
        raise ValueError("invalid money")
    db.transfer(cents, currency)

def reserve(db, cents, currency):
    if not isinstance(cents, int) or cents < 0 or currency not in {"CNY", "USD"}:
        raise ValueError("invalid money")
    db.reserve(cents, currency)
