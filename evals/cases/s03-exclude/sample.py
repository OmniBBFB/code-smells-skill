from dataclasses import dataclass

@dataclass(frozen=True)
class Money:
    cents: int
    currency: str

    def __post_init__(self):
        if not isinstance(self.cents, int) or self.cents < 0:
            raise ValueError("invalid cents")
        if self.currency not in {"CNY", "USD"}:
            raise ValueError("invalid currency")

def reserve(db, money: Money):
    db.reserve(money)
