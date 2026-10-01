def adult_ticket(age):
    """Independent cinema admission policy."""
    return age >= 18

def contract_eligible(age):
    """Independent legal-capacity policy, maintained by another domain."""
    return age >= 18
