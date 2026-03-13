import pandas as pd
fd = pd.read_csv('er.csv')
fd['total'] = fd['m1'] + fd['m2']
fd['avg'] = fd['total'] / 2
fd['result'] = (fd['m1'] > 34.4) & (fd['m2'] > 34.4)
fd['result'] = fd['result'].apply(lambda x: 'Pass' if x == True else 'Fail')
print(fd)
'''
    rno sname  m1    m2  total    avg result
0  1001    x1  45  54.5   99.5  49.75   Pass
1  1002    x3  61  54.0  115.0  57.50   Pass
2  1003    x5  77  63.0  140.0  70.00   Pass
3  1004    x2  98  20.0  118.0  59.00   Fail
4  1005    x4  52  36.0   88.0  44.00   Pass
'''