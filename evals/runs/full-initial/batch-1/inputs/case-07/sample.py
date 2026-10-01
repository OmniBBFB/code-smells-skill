def increment(raw):
    # This local wrapper has no external consumer or special type contract.
    class Box:
        def __init__(self, value):
            self.value = value
    wrapped = Box(raw)
    return wrapped.value + 1
