import requests
import json
from a2requeststatus import *
BASE_URL = "http://127.0.0.1:1234/er"
header = {"Content-Type": "application/json"}
erNewRow = {"rno": 1001, "sname": "x5", "m1": 56.5, "m2": 63}
try:
    res = requests.post(BASE_URL, data=json.dumps(erNewRow), headers=header)
    res.raise_for_status()
    uRequestStatus(res)
except Exception as e:
    print("Err.", e)
'''
JSON:
{'m1': 56.5, 'm2': 63, 'rno': 1001, 'sname': 'x5'}

TEXT:
{
  "m1": 56.5,
  "m2": 63,
  "rno": 1001,
  "sname": "x5"
}

Request Body:
{"rno": 1001, "sname": "x5", "m1": 56.5, "m2": 63}
Status Code:
201
Method:
<PreparedRequest [POST]>
URL:
http://127.0.0.1:1234/er
Headers:
{'User-Agent': 'python-requests/2.32.5', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Content-Length': '50'}

'''