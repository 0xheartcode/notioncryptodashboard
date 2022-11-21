import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

import json
import requests

token = os.environ.get('NOTION_KEY') 
database_id = os.environ.get('NOTION_DATABASE_ID')


print(os.environ.get('NOTION_KEY'))


headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {token}",
    "Notion-Version": "2022-06-28"
    }

url = f'https://api.notion.com/v1/databases/{database_id}/query'


payload = {
    "page_size": 100,
    "filter": {
        "property": "CoingeckoID",
        "rich_text": {
            "contains": "koinos"
            }
        }
}

response = requests.post(url, json=payload, headers=headers)

cleanJson = json.dumps(response.json(), indent=1)

print(cleanJson)




