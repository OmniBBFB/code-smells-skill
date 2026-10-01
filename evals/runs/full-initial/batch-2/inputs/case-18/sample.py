def run(value, transform):
    """Public contract supports caller-selected output policies."""
    return transform(value + 1)

def sample(value):
    return run(value, str), run(value, lambda x: x * 2)
