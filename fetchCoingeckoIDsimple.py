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
}

response = requests.post(url, json=payload, headers=headers)

# standard output line
# cleanJson = json.dumps(response.json(), indent=1)

cleanJson = json.dumps(response.json()["results"], indent=1)

# get clean rich_text content and not plain text
# cleanJson = json.dumps(response.json()["results"][0]["properties"]["CoingeckoID"]["rich_text"][0]["text"]["content"], indent=1)



# get clean plain text from json output, line below:
# cleanJson = json.dumps(response.json()["results"][0]["properties"]["CoingeckoID"]["rich_text"][0]["plain_text"], indent=1)

# print(cleanJson)
for i in response.json()["results"]:
    subdata = i["properties"]["CoingeckoID"]["rich_text"]
    # python implicit, if list is not empty. the inverse would be `if not subdata`
    if subdata:
        subsubdata = subdata[0]["plain_text"]
        print(subsubdata)

    # print(i["properties"]["CoingeckoID"]["rich_text"], indent=1)
    # This code works, but seems to give an error if we go deeper in the JSON structure if the variable is empty.

    #It seems a dictionary with multiple values might be the solution in this case. The key will either be the coingeckoID or the name of the token, the first 'mapping' or dictionnary value will be between the coingeckoID and the different values. The second 'mapping' will be between the coingeckoID and the name. The problem would be, how do we update the table if we have a column without a coingeckoID or with a wrong coingeckoID...

    #Test case 1) the coingeckoID exists and it is correct. Test should work to fetch and update live data.

    #Test case 2) coingeckoID is wrong, test should fail, and say the coingeckoID does not exist but still update the other values.

    #Test case 3) same, but it is empty instead of wrong. It should simply skip this column. Perhaps give a troubleshooting warning.

