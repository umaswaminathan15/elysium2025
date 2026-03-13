import pandas as pd
fd = pd.read_csv('examresult.csv')
print(fd.dtypes)
fd = pd.read_csv('er.csv')
print(fd.dtypes)
'''
rno          int64
sname          str
m1           int64
m2         float64
total      float64
average    float64
result         str
dtype: object
rno        int64
sname        str
m1         int64
m2       float64
dtype: object
'''