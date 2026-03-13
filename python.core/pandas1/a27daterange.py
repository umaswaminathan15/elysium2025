import pandas as pd
dr = pd.DataFrame()
dr['rng'] = pd.date_range('12/31/2010',periods=5, freq='90s')
print(dr['rng'].dt.day)
print(dr['rng'].dt.month)
print(dr['rng'].dt.year)
print(dr['rng'].dt.hour)
print(dr['rng'].dt.minute)
print(dr['rng'].dt.second)
'''
0    31
1    31
2    31
3    31
4    31
Name: rng, dtype: int32
0    12
1    12
2    12
3    12
4    12
Name: rng, dtype: int32
0    2010
1    2010
2    2010
3    2010
4    2010
Name: rng, dtype: int32
0    0
1    0
2    0
3    0
4    0
Name: rng, dtype: int32
0    0
1    1
2    3
3    4
4    6
Name: rng, dtype: int32
0     0
1    30
2     0
3    30
4     0
Name: rng, dtype: int32
'''