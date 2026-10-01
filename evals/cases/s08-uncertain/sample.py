from vendor import BaseStorage

class Archive(BaseStorage):
    def write(self, data):
        raise NotImplementedError("read-only")
# vendor base contract is not provided.
