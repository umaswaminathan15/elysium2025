import requests
import json
from a2requeststatus import *

BASE_URL = 'http://127.0.0.1:1234/er/1002'
headerJSON = {"Content-Type": "application/json"}
erEditRow = {"sname": "t2"}
try:
    res = requests.patch(BASE_URL,data=json.dumps(erEditRow), headers=headerJSON)
    res.raise_for_status()
    uRequestStatus(res)
except Exception as e:
    print("Err.", e)
'''
Err. 405 Client Error: METHOD NOT ALLOWED for url: http://127.0.0.1:1234/er/1002
'''
