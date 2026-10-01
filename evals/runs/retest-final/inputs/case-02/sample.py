def reserve(client, amount, unit):
    if amount < 0 or unit not in {1, 2}:
        raise ValueError("invalid amount/unit")
    return client.reserve(amount, unit)

def transfer(client, amount, unit):
    if amount < 0 or unit not in {1, 2}:
        raise ValueError("invalid amount/unit")
    return client.transfer(amount, unit)

# Whether amount/unit are domain values or a fixed raw wire format is unavailable.
# Public boundary and ownership of these constraints are not supplied.
