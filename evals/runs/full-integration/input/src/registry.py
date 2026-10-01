from lifecycle import after_checkout

EVENTS = {"checkout-completed": after_checkout}


def dispatch(event_type, event):
    return EVENTS[event_type](event)
