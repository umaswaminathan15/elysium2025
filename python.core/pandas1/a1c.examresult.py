import pandas as pd
fd = pd.read_csv('examresult.csv')
print(fd.head(3).tail(1))
print(fd.tail(3).head(1))
'''
    rno sname  m1    m2  total  average result
2  1003    x5  77  63.0  140.0     70.0   Pass
    rno sname  m1    m2  total  average result
2  1003    x5  77  63.0  140.0     70.0   Pass
'''