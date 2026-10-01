def connect(host, port, tls):
    """host/port/tls together identify one service endpoint."""
    return (host, port, tls)

def check(host, port, tls):
    return connect(host, port, tls) is not None

def fetch(host, port, tls, key):
    endpoint = connect(host, port, tls)
    return endpoint, key

def refresh(host, port, tls):
    return fetch(host, port, tls, "status")
