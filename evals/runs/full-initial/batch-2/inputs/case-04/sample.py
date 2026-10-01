class Storage:
    """Every subtype supports writing nonempty bytes with no extra restriction."""
    def write(self, data):
        raise NotImplementedError

class ReadOnlyStorage(Storage):
    def write(self, data):
        raise RuntimeError("writing unsupported")

def backup(storage: Storage):
    storage.write(b"backup")
