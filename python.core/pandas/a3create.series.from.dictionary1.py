import pandas as pd
d = {'eid' : 1001, 'ename' : 'x5', 'sal' : 500000}
s = pd.Series(d)
print(d)
print(s)
d = {'eid' : 1001, 'sal' : 500000}
s = pd.Series(d)
print(d)
print(s)
d = {'eid' : 1001, 'sal' : 500000.0}
s = pd.Series(d)
print(d)
print(s)
d = {'eid' : 1001, 'sal' : 500000}
s = pd.Series(d)
print(d)
print(s)
'''
{'eid': 1001, 'ename': 'x5', 'sal': 500000}
eid        1001
ename        x5
sal      500000
dtype: object
{'eid': 1001, 'sal': 500000}
eid      1001
sal    500000
dtype: int64
{'eid': 1001, 'sal': 500000.0}
eid      1001.0
sal    500000.0
dtype: float64
{'eid': 1001, 'sal': 500000}
eid      1001
sal    500000
dtype: int64
'''