import requests
from a2requeststatus import *

BASE_URL = 'http://127.0.0.1:1234/er/1002'
headerJSON = {"Content-Type": "application/json"}
try:
    res = requests.get(BASE_URL, headers=headerJSON)
    uRequestStatus(res)
except Exception as e:
    print("Err.", e)
'''
JSON:
{'m1': 98, 'm2': 20, 'rno': 1002, 'sname': 'x2'}

TEXT:
{
  "m1": 98,
  "m2": 20,
  "rno": 1002,
  "sname": "x2"
}

Request Body:
None
Status Code:
200
Method:
<PreparedRequest [GET]>
URL:
http://127.0.0.1:1234/er/1002
Headers:
{'User-Agent': 'python-requests/2.32.5', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Type': 'application/json'}
'''