class Session:
    def __init__(self):
        self.pending = None

    def amount(self):
        return self.pending.total
# Lifecycle, writers and state protocol are unavailable.
