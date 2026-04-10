import os
from functions.calc.calcFunctions import CalcFunction
from functions.notifications.sendNotification import MailNotification
from api.notion.client import NotionClient
from api.notion.models.status import Status
from api.notion.models.mail_templates import MailTemplate
from api.notion import databases
from api.notion import pages

NOTION_DATABASE_ID = os.environ['NOTION_DATABASE_ID']

client = NotionClient()
mail = MailNotification(
    sender_email=os.environ['GOOGLE_MAIL'],
    password=os.environ['GOOGLE_APP_PWD']
)

db_entries = databases.getDatabase(client, NOTION_DATABASE_ID)['results']

for entry in db_entries:
    end_date = entry['properties']['Ablaufdatum']['date']['start']
    start_date = entry['properties']['Ablaufdatum']['date']['start']
    product = entry['properties']['Produkt']['title'][0]['text']['content']
    page_id = entry['id']

    current_status = entry['properties']['Status']['status']['name']
    new_status = None

    days_diff = CalcFunction.getDiffFromNow(date=end_date)
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
    elif current_status == 'Open': #and CalcFunction.getDiffFromNow(date=start_date) == 0:
        pages.setPageStatus(client, page_id, Status.ACTIVE.value)
        print(f'Id: {page_id} - Status Changed from OPEN to ACTIVE')
    
    if new_status and new_status.value != current_status:
        pages.setPageStatus(client, page_id, new_status.value)
        context = {
            "Produkt": product,
            "Ablaufdatum": end_date
        }
        mail.sendNotification(
            status=new_status,
            reciver_email=os.environ['GOOGLE_MAIL'],
            context=context
        )
