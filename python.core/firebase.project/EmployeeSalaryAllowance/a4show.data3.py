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
def str2float(s):
    try:
        return float(s)
    except:
        return 0
print(f"{'rno':<10}{'ename':<10}{'sal':<10}{'hra':<10}{'da':<10}{'pf':<10}{'gpay':<10}{'npay':<10}")
try:
    fb = pyrebase.initialize_app(fbConfig)
    db = fb.database()
    rows = db.get()
    for row in rows.each():
        dic = row.val()
        rno = row.key()
        ename = dic['ename']
        sal = str2float(dic['sal'])
        hra = sal * 20/100
        da = sal * 15/100
        pf = sal * 35/100
        gpay =sal + hra + da
        npay = gpay - pf
        print(f"{rno:<10}{ename:<10}{sal:<10}{hra:<10}{da:<10}{pf:<10}{gpay:<10}{npay:<10}")
except Exception as e:
    print("Err.", e)
'''
rno       ename     sal       hra       da        pf        gpay      npay      
1001      x5        500000.0  100000.0  75000.0   175000.0  675000.0  500000.0  
1002      x3        300000.0  60000.0   45000.0   105000.0  405000.0  300000.0  
1003      x1        100000.0  20000.0   15000.0   35000.0   135000.0  100000.0  
1004      x2        200000.0  40000.0   30000.0   70000.0   270000.0  200000.0  
1005      x4        400000.0  80000.0   60000.0   140000.0  540000.0  400000.0  

'''
