def queryDatabase(client, database_id, payload=None):
    return client.request(
        "POST",
        f"databases/{database_id}/query",
        payload
    )