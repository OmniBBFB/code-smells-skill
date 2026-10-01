class CustomerId:
    """Validated identity type used to prevent mixing customer and invoice IDs."""
    def __init__(self, value):
        if not value.startswith("customer:"):
            raise ValueError("invalid identity")
        self.value = value
