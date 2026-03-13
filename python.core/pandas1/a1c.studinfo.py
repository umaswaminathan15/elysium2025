import pandas as pd
fd = pd.read_csv('studinfo.csv')
fd['dob'] = pd.to_datetime(fd.dob)
print(fd)
print(fd.dob.dt.hour)
print(fd.dob.dt.dayofyear)
'''
    rno sname                 dob
0  1001    x1 1990-10-15 01:00:00
1  1002    x3 1990-09-10 21:00:00
2  1003    x5 1990-10-15 02:00:00
3  1004    x2 1990-09-10 20:00:00
4  1005    x4 1990-11-25 03:00:00
0     1
1    21
2     2
3    20
4     3
Name: dob, dtype: int32
0    288
1    253
2    288
3    253
4    329
Name: dob, dtype: int32
'''