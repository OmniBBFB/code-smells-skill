class Shipment:
    """Local shipping types; adding a carrier requires its fee and transit time."""
    def __init__(self, kind):
        self.kind = kind

def fee(shipment):
    if shipment.kind == "air": return 30
    if shipment.kind == "road": return 10
    raise ValueError("unknown carrier")

def days(shipment):
    if shipment.kind == "air": return 1
    if shipment.kind == "road": return 4
    raise ValueError("unknown carrier")
