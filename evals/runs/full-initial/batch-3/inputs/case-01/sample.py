from dataclasses import dataclass

@dataclass(frozen=True)
class Endpoint:
    host: str
    port: int
    tls: bool

def connect(endpoint: Endpoint):
    return endpoint

def fetch(endpoint: Endpoint, key):
    return connect(endpoint), key
