import pandas as pd
L = [
    [1001, 11],
    [1002, 22],
    [1003, 33]
]
print(L)
df = pd.DataFrame(L)
print(df)
print(df[1])
'''

[[1001, 11], [1002, 22], [1003, 33]]
      0   1
0  1001  11
1  1002  22
2  1003  33
0    11
1    22
2    33
Name: 1, dtype: int64'''