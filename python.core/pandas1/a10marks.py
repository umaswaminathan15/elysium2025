import pandas as pd
d = {
    'x3':[45.5,70],
    'x1':[52,43.0],
    'x2':[98,20]
}
df = pd.DataFrame(d)
print(df)
print(df['x1'])
'''
     x3    x1  x2
0  45.5  52.0  98
1  70.0  43.0  20
0    52.0
1    43.0
Name: x1, dtype: float64
'''