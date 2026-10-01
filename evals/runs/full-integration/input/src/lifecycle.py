def after_checkout(event):
    return {"receipt": event["order_id"]}
