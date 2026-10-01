class LocalSms:
    """Delivers one text body to one phone, returning a message id."""
    def send(self, phone, body):
        return phone + body

class LocalBackupSms:
    """Same delivery and failure contract as LocalSms; owned in this project."""
    def transmit(self, body, phone):
        return phone + body

def notify(client, phone, body):
    if isinstance(client, LocalSms):
        return client.send(phone, body)
    return client.transmit(body, phone)
