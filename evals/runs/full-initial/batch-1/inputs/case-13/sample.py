def provider_timeout_seconds():
    # The vendor closes idle sessions after 30 seconds; leave headroom for cleanup.
    # Reference: the supplied integration contract fixes this deadline.
    return 25
