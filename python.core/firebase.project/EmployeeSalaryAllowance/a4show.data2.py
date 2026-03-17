import pyrebase
fbConfig = {
    "apiKey": "AIzaSyAgkHNtFZaGgzb2vOIQsAsfwq0rizaPkwU",
    "authDomain": "fbprj1a-e3931.firebaseapp.com",
    "databaseURL": "https://fbprj1a-e3931-default-rtdb.firebaseio.com",
  "projectId": "fbprj1a-e3931",
  "storageBucket": "fbprj1a-e3931.firebasestorage.app",
  "messagingSenderId": "515148740856",
  "appId": "1:515148740856:web:7859f9485892594822630d"
}
try:
    fb = pyrebase.initialize_app(fbConfig)
    db = fb.database()
    rows = db.get()
    for r in rows.each():
        print(r.key(), r.val())
except Exception as e:
    print("Err.", e)
'''
1001 {'ename': 'x5', 'sal': '500000'}
1002 {'ename': 'x3', 'sal': '300000'}
1003 {'ename': 'x1', 'sal': '100000'}
1004 {'ename': 'x2', 'sal': '200000'}
1005 {'ename': 'x4', 'sal': '400000'}
'''