import requests
import json
from a2requeststatus import *

BASE_URL = 'http://127.0.0.1:1234/er'
headerJSON = {"Content-Type": "application/json"}
erNewRows = [
    {"rno": 1003, "sname": "x3", "m1": 45.5, "m2": 52},
    {"rno": 1005, "sname": "x1", "m1": 61, "m2": 54.5},
    {"rno": 1002, "sname": "x2", "m1": 98, "m2": 20},
    {"rno": 1004, "sname": "x4", "m1": 54.5, "m2": 38.5},
]
try:
    for erNewRow in erNewRows:
        res = requests.post(BASE_URL, data=json.dumps(erNewRow), headers=headerJSON)
        res.raise_for_status()
        uRequestStatus(res)
except Exception as e:
    print("Err.", e)
'''
"C:\Program Files\Python313\python.exe" D:\su\python2\flask.restapi\a2\b2post.py 
JSON:
{'m1': 45.5, 'm2': 52, 'rno': 1003, 'sname': 'x3'}

TEXT:
{
  "m1": 45.5,
  "m2": 52,
  "rno": 1003,
  "sname": "x3"
}

Request Body:
{"rno": 1003, "sname": "x3", "m1": 45.5, "m2": 52}
Status Code:
201
Method:
<PreparedRequest [POST]>
URL:
http://127.0.0.1:1234/er
Headers:
{'User-Agent': 'python-requests/2.32.5', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Content-Length': '50'}
JSON:
{'m1': 61, 'm2': 54.5, 'rno': 1005, 'sname': 'x1'}

TEXT:
{
  "m1": 61,
  "m2": 54.5,
  "rno": 1005,
  "sname": "x1"
}

Request Body:
{"rno": 1005, "sname": "x1", "m1": 61, "m2": 54.5}
Status Code:
201
Method:
<PreparedRequest [POST]>
URL:
http://127.0.0.1:1234/er
Headers:
{'User-Agent': 'python-requests/2.32.5', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Content-Length': '50'}
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
{"rno": 1002, "sname": "x2", "m1": 98, "m2": 20}
Status Code:
201
Method:
<PreparedRequest [POST]>
URL:
http://127.0.0.1:1234/er
Headers:
{'User-Agent': 'python-requests/2.32.5', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Content-Length': '48'}
JSON:
{'m1': 54.5, 'm2': 38.5, 'rno': 1004, 'sname': 'x4'}

TEXT:
{
  "m1": 54.5,
  "m2": 38.5,
  "rno": 1004,
  "sname": "x4"
}

Request Body:
{"rno": 1004, "sname": "x4", "m1": 54.5, "m2": 38.5}
Status Code:
201
Method:
<PreparedRequest [POST]>
URL:
http://127.0.0.1:1234/er
Headers:
{'User-Agent': 'python-requests/2.32.5', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Content-Length': '52'}

Process finished with exit code 0

'''