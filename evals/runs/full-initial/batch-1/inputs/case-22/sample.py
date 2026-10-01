def restore_balance(wallet, snapshot):
    wallet._balance = snapshot["balance"]
