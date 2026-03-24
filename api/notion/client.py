import os
import requests

class NotionClient:
    BASE_URL = "https://api.notion.com/v1"

    def __init__(self, secret=None):
        self.secret = secret or os.getenv('SECRET')
        self.headers = {
            "Notion-Version": "2022-06-28",
            "Authorization": f"Bearer {self.secret}",
            "Content-Type": "application/json"
        }

    def request(self, method, endpoint, payload=None):
        url = f"{self.BASE_URL}/{endpoint}"

        response = requests.request(
            method=method,
            url=url,
            headers=self.headers,
            json=payload
        )

        response.raise_for_status()
        return response.json()