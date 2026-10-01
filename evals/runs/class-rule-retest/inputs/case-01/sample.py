class Checkout:
    """Coordinates separately owned pricing, storage and presentation rules."""
    def __init__(self, pricing, store, renderer):
        self.pricing = pricing
        self.store = store
        self.renderer = renderer

    def run(self, order):
        result = self.pricing.quote(order)
        self.store.save(result)
        return self.renderer.render(result)
