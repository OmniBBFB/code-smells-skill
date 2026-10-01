from dataclasses import dataclass

@dataclass(frozen=True)
class AccountView:
    """Read-only JSON projection; domain writes live in a different model."""
    limit: int
    spent: int

def serialize(view):
    return {"limit": view.limit, "spent": view.spent}
