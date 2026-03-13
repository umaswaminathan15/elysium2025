import pandas as pd
fp = 'examresult.csv'
fd = pd.read_csv(fp)
print(fd)
'''
    rno sname  m1    m2  total  average result
0  1001    x1  45  54.5   99.5    49.75   Pass
1  1002    x3  61  54.0  115.0    57.50   Pass
2  1003    x5  77  63.0  140.0    70.00   Pass
3  1004    x2  98  20.0  118.0    59.00   Pass
4  1005    x4  52  36.0   88.0    44.00   Fail
'''