import pandas as pd
fd = pd.read_csv('examresult.csv')
print(fd.head(2))
print(fd.tail(2))
'''
    rno sname  m1    m2  total  average result
0  1001    x1  45  54.5   99.5    49.75   Pass
1  1002    x3  61  54.0  115.0    57.50   Pass
    rno sname  m1    m2  total  average result
3  1004    x2  98  20.0  118.0     59.0   Pass
4  1005    x4  52  36.0   88.0     44.0   Fail

'''