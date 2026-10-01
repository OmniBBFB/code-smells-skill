class Sms:
    """Local delivery port."""
    def send(self, phone, body):
        raise NotImplementedError

class VendorSmsAdapter(Sms):
    def __init__(self, external):
        self.external = external

    def send(self, phone, body):
        return self.external.transmit(body, phone)

def notify(client: Sms, phone, body):
    return client.send(phone, body)
