import pyrebase
row1 = {
    "rno": "1001",
    "ename": "x5",
    "sal": "500000"
}
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
    db.push(row1)
    print('Added one row')
except Exception as e:
    print("Err.", e)
'''
Added one row
'''