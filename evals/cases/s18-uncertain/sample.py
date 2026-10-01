def process(value, before=None, after=None):
    if before:
        before(value)
    if after:
        after(value)
    return value
# Consumers, public API commitments and extension configuration are unavailable.
