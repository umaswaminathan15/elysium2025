import pandas as pd
fd = pd.read_csv('studinfo.csv')
print(fd)
print(fd.dtypes)
'''
    rno sname               dob
0  1001    x1  15-10-1990 01:00
1  1002    x3  10-09-1990 21:00
2  1003    x5  15-10-1990 02:00
3  1004    x2  10-09-1990 20:00
4  1005    x4  25-11-1990 03:00
rno      int64
sname      str
dob        str
dtype: object
'''