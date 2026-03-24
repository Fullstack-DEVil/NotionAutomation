import os
from dotenv import load_dotenv
from api.notion.client import NotionClient
from api.notion import databases

load_dotenv()

DATABASE_ID = os.getenv('DATABASE_ID')

client = NotionClient()

data = databases.queryDatabase(client, DATABASE_ID)

print(data)