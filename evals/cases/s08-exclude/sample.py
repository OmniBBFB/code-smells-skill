class Storage:
    """write may explicitly report Unsupported; callers must handle it."""
    def write(self, data):
        raise NotImplementedError

class ReadOnlyStorage(Storage):
    def write(self, data):
        return "Unsupported"

def backup(storage: Storage):
    return storage.write(b"backup")
