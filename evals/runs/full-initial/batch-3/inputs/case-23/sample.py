class PriceCalculator:
    def __init__(self):
        self._running_sum = None
        self._running_tax = None

    def prepare(self, prices):
        self._running_sum = sum(prices)
        self._running_tax = self._running_sum * 0.1

    def finish(self):
        return self._running_sum + self._running_tax

def quote(prices):
    calculator = PriceCalculator()
    calculator.prepare(prices)
    return calculator.finish()
