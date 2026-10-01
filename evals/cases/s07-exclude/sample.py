class Document:
    """Cached digest is optional state valid throughout this object's life."""
    def __init__(self, text):
        self.text = text
        self._digest = None

    def digest(self):
        if self._digest is None:
            self._digest = hash(self.text)
        return self._digest
