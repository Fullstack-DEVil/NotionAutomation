import os
from dotenv import load_dotenv
from functions.calc.calcFunctions import CalcFunction
from api.notion.client import NotionClient
from api.notion.models.status import Status
from api.notion import databases
from api.notion import pages

load_dotenv()

DATABASE_ID = os.getenv('DATABASE_ID')

client = NotionClient()

db_entries = databases.getDatabase(client, DATABASE_ID)['results']

for entry in db_entries:
    date = entry['properties']['Ablaufdatum']['date']['start']
    page_id = entry['id']
    days_deff = CalcFunction.getDiffFromNow(date=date)