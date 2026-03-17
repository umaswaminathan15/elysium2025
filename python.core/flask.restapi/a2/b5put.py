import requests
import json
from a2requeststatus import *

BASE_URL = 'http://127.0.0.1:1234/er/1002'
headerJSON = {"Content-Type": "application/json"}
erEditRow = {"sname":"x2", "m1": 43, "m2": 49.5}
try:
    res = requests.put(BASE_URL, data=json.dumps(erEditRow), headers=headerJSON)
    res.raise_for_status()
    uRequestStatus(res)
except Exception as e:
    print("Err.", e)
'''
JSON:
{'m1': 43, 'm2': 49.5, 'rno': 1002, 'sname': 'x2'}

TEXT:
{
  "m1": 43,
  "m2": 49.5,
  "rno": 1002,
  "sname": "x2"
}

Request Body:
{"sname": "x2", "m1": 43, "m2": 49.5}
Status Code:
200
Method:
<PreparedRequest [PUT]>
URL:
http://127.0.0.1:1234/er/1002
Headers:
{'User-Agent': 'python-requests/2.32.5', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Content-Length': '37'}

'''
