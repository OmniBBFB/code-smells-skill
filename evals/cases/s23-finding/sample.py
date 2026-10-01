class VendorDay:
    """Supplied frozen third-party API; only y/m/d accessors, cannot be edited."""
    def __init__(self, y, m, d):
        self.y, self.m, self.d = y, m, d

def receipt_day(day: VendorDay):
    return f"{day.y:04}-{day.m:02}-{day.d:02}"

def export_day(day: VendorDay):
    return f"{day.y:04}-{day.m:02}-{day.d:02}"

# Both callers require the same ISO date representation, absent from this API.
