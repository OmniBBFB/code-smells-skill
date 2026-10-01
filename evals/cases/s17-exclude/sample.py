HANDLERS = {}

def register(name):
    def decorate(fn):
        HANDLERS[name] = fn
        return fn
    return decorate

@register("ping")
def ping():
    return "pong"

def dispatch(name):
    return HANDLERS[name]()
