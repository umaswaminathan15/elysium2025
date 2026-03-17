import requests
from a2requeststatus import *

BASE_URL = 'http://127.0.0.1:1234/er'
headerJSON = {"Content-Type": "application/json"}
try:
    res = requests.get(BASE_URL, headers=headerJSON)
    uRequestStatus(res)
except Exception as e:
    print("Err.", e)

'''
"C:\Program Files\Python313\python.exe" D:\su\python2\flask.restapi\a2\b3get.py 
JSON:
[{'m1': 56.5, 'm2': 63, 'rno': 1001, 'sname': 'x5'}, {'m1': 45.5, 'm2': 52, 'rno': 1003, 'sname': 'x3'}, {'m1': 61, 'm2': 54.5, 'rno': 1005, 'sname': 'x1'}, {'m1': 98, 'm2': 20, 'rno': 1002, 'sname': 'x2'}, {'m1': 54.5, 'm2': 38.5, 'rno': 1004, 'sname': 'x4'}]

TEXT:
[
  {
    "m1": 56.5,
    "m2": 63,
    "rno": 1001,
    "sname": "x5"
  },
  {
    "m1": 45.5,
    "m2": 52,
    "rno": 1003,
    "sname": "x3"
  },
  {
    "m1": 61,
    "m2": 54.5,
    "rno": 1005,
    "sname": "x1"
  },
  {
    "m1": 98,
    "m2": 20,
    "rno": 1002,
    "sname": "x2"
  },
  {
    "m1": 54.5,
    "m2": 38.5,
    "rno": 1004,
    "sname": "x4"
  }
]

Request Body:
None
Status Code:
200
Method:
<PreparedRequest [GET]>
URL:
http://127.0.0.1:1234/er
Headers:
{'User-Agent': 'python-requests/2.32.5', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Type': 'application/json'}

Process finished with exit code 0

'''
