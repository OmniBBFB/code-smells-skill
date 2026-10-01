class VendorDay:
    """Supplied third-party API includes ISO formatting."""
    def __init__(self, y, m, d):
        self.y, self.m, self.d = y, m, d

    def isoformat(self):
        return f"{self.y:04}-{self.m:02}-{self.d:02}"

def receipt_day(day: VendorDay):
    return day.isoformat()
