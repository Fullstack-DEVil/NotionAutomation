def setPageStatus(client, page_id, status):
    payload = {
        "properties": {
            "Status": {
                "status": {
                    "name": status
                }
            }
        }
    }
    return client.request(
        "PATCH",
        f"pages/{page_id}",
        payload
    )