def run(value):
    # Entire private flow: no export or configurable caller exists.
    def compute(number, transform=None, before=None, after=None):
        if before is not None:
            before(number)
        result = number + 1
        if transform is not None:
            result = transform(result)
        if after is not None:
            after(result)
        return result
    return compute(value)
