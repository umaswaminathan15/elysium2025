import pandas as pd
Ldat = ['x5', 'x3', 'x1', 'x2', 'x4']
Lidx = [1001, 1002, 1003, 1004, 1005]
s = pd.Series(data=Lidx, index=Ldat)
print(s)
print(s[:-2])
print(['x1'])
print(s[['x1', 'x2', 'x3', 'x4', 'x5']])
s = pd.Series(data=Ldat, index=Lidx)
print(s)
print(s[:-2])
'''
x5    1001
x3    1002
x1    1003
x2    1004
x4    1005
dtype: int64
x5    1001
x3    1002
x1    1003
dtype: int64
['x1']
x1    1003
x2    1004
x3    1002
x4    1005
x5    1001
dtype: int64
1001    x5
1002    x3
1003    x1
1004    x2
1005    x4
dtype: str
1001    x5
1002    x3
1003    x1
dtype: str
'''