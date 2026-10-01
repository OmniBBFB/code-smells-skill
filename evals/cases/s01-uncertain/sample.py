def complete_job(records, store, sender):
    # Only this excerpt of the implementation is available.
    clean = store.prepare(records)
    ...
    sender.send(clean)
