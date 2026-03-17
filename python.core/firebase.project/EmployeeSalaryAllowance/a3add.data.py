import pyrebase
rows = [
    {"ename": "x5", "sal": "500000"},
    {"ename": "x3", "sal": "300000"},
    {"ename": "x1", "sal": "100000"},
    {"ename": "x2", "sal": "200000"},
    {"ename": "x4", "sal": "400000"}

]
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
    rno = 1001
    fb = pyrebase.initialize_app(fbConfig)
    db = fb.database()
    for row in rows:
        db.child(str(rno)).set(row)
        rno += 1
    print("Added five row(s)")
except Exception as e:
    print("Err.", e)
'''
Added five row(s)
'''