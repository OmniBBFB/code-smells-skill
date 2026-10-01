def prepare_delivery(sender_name, sender_phone, receiver_name, receiver_phone,
                     street, city, postal_code, carrier, insured, urgent):
    """Positional contract used by local clients; recipient details evolve together."""
    return {
        "sender": (sender_name, sender_phone),
        "recipient": (receiver_name, receiver_phone, street, city, postal_code),
        "service": (carrier, insured, urgent),
    }

def sample():
    return prepare_delivery("A", "111", "B", "222", "Main", "X", "123",
                            "road", True, False)
