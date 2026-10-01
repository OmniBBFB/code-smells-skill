def result(client):
    return client.get_user().profile().address().city()
