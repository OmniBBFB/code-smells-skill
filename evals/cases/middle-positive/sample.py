class RowStore:
    def __init__(self):
        self.rows = {}

    def get(self, key):
        return self.rows[key]

    def put(self, key, value):
        self.rows[key] = value

def lookup(store: RowStore, key):
    class Bridge:
        def __init__(self, target):
            self.target = target

        def get(self, key):
            return self.target.get(key)

        def put(self, key, value):
            return self.target.put(key, value)

    return Bridge(store).get(key)
