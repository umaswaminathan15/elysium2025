import pandas as pd
fd = pd.read_csv('examresult.csv')
print(fd['rno'])
print(fd['sname'])
print(fd['m1'])
print(fd['m2'])
'''
0    1001
1    1002
2    1003
3    1004
4    1005
Name: rno, dtype: int64
0    x1
1    x3
2    x5
3    x2
4    x4
Name: sname, dtype: str
0    45
1    61
2    77
3    98
4    52
Name: m1, dtype: int64
0    54.5
1    54.0
2    63.0
3    20.0
4    36.0
Name: m2, dtype: float64
'''