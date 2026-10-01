class Query:
    """Fluent query builder; each method returns this same instance."""
    def __init__(self):
        self.steps = []

    def filter(self, **conditions):
        self.steps.append(("filter", conditions))
        return self

    def order_by(self, field):
        self.steps.append(("order", field))
        return self

    def limit(self, count):
        self.steps.append(("limit", count))
        return self

def active_users(query):
    return query.filter(active=True).order_by("name").limit(20)
