import requests
import json
from a2requeststatus import *

BASE_URL = 'http://127.0.0.1:1234/er/1003'
headerJSON = {"Content-Type": "application/json"}
try:
    res = requests.delete(BASE_URL, headers=headerJSON)
    res.raise_for_status()
    uRequestStatus(res)
except Exception as e:
    print("Err.", e)
'''
JSON:
{'message': '1003 deleted'}

TEXT:
{
  "message": "1003 deleted"
}

Request Body:
None
Status Code:
200
Method:
<PreparedRequest [DELETE]>
URL:
http://127.0.0.1:1234/er/1003
Headers:
{'User-Agent': 'python-requests/2.32.5', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Content-Length': '0'}

'''