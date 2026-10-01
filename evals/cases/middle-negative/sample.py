class RepositoryPort:
    """Stable application boundary; callers never depend on backend APIs."""
    def find(self, key):
        raise NotImplementedError

class SqlRepository(RepositoryPort):
    def __init__(self, db):
        self.db = db

    def find(self, key):
        return self.db.fetch_row(key)

class MemoryRepository(RepositoryPort):
    def __init__(self, rows):
        self.rows = rows

    def find(self, key):
        return self.rows[key]

def load(repo: RepositoryPort, key):
    return repo.find(key)
