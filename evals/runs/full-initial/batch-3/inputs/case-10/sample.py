class Gateway:
    def __init__(self, backend):
        self.backend = backend

    def fetch(self, key):
        return self.backend.fetch(key)

    def save(self, record):
        return self.backend.save(record)
