def parse_boolean(token):
    """Single decoding boundary for a fixed external wire format."""
    match token:
        case "1": return True
        case "0": return False
        case _: raise ValueError("invalid boolean")
