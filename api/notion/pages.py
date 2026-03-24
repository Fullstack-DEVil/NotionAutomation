import requests
import os
import datetime
from dotenv import load_dotenv

load_dotenv()
url = f"https://api.notion.com/v1/databases/{os.getenv('DATABASE_ID')}/query"

headers = {
    "Notion-Version": "2022-06-28",
    "Authorization": f"Bearer {os.getenv('SECRET')}",
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers)
data = response.json()

now = datetime.datetime.now()
count = 0

for result in data['results']:
    print(result['properties']['Ablaufdatum']['date']['start'])
    date_value = datetime.datetime.fromisoformat(result['properties']['Ablaufdatum']['date']['start'])
    delta = date_value - now
    print(f"Ablaufdatum: {date_value} | Differenz in Tagen (dezimal): {delta}")
    if (delta.total_seconds()/86400.0) >= 30:
        count += 1

print(f"Anzahl abgelaufener Einträge: {count}")