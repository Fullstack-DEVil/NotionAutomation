import os
from dotenv import load_dotenv
from functions.calc.calcFunctions import CalcFunction
from functions.notifications.sendNotification import MailNotification
from api.notion.client import NotionClient
from api.notion.models.status import Status
from api.notion.models.mail_templates import MailTemplate
from api.notion import databases
from api.notion import pages

load_dotenv()

DATABASE_ID = os.getenv('DATABASE_ID')

client = NotionClient()
mail = MailNotification(
    sender_email=os.getenv('EMAIL'),
    password=os.getenv('PWD')
)

db_entries = databases.getDatabase(client, DATABASE_ID)['results']
print(db_entries)

for entry in db_entries:
    date = entry['properties']['Ablaufdatum']['date']['start']
    product = entry['properties']['Produkt']['title'][0]['text']['content']
    page_id = entry['id']

    current_status = entry['properties']['Status']['status']['name']
    new_status = None

    days_diff = CalcFunction.getDiffFromNow(date=date)
    if current_status == 'Active' or current_status.startswith('Expires'):
        if days_diff == 30:
            new_status = Status.EXPIRES_30
        elif days_diff == 15:
            new_status = Status.EXPIRES_15
        elif days_diff == 10:
            new_status = Status.EXPIRES_10
        elif days_diff == 5:
            new_status = Status.EXPIRES_5
        elif days_diff == 3:
            new_status = Status.EXPIRES_3
        elif days_diff == 2:
            new_status = Status.EXPIRES_2
        elif days_diff == 1:
            new_status = Status.EXPIRES_1
        else:
            print(f'Id: {page_id} - Status: {Status.ACTIVE.value} - Expired in {days_diff} day(s)')
    
    if new_status and new_status.value != current_status:
        pages.setPageStatus(client, page_id, new_status.value)
        context = {
            "Produkt": product,
            "Ablaufdatum": date
        }
        mail.sendNotification(
            status=new_status,
            reciver_email=os.getenv('EMAIL'),
            context=context
        )
