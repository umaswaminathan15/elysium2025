import pandas as pd
dr = pd.DataFrame()
dr['rng'] = pd.date_range('12/31/2010',periods=5, freq='90s')
print(dr['rng'])
'''
0   2010-12-31 00:00:00
1   2010-12-31 00:01:30
2   2010-12-31 00:03:00
3   2010-12-31 00:04:30
4   2010-12-31 00:06:00
Name: rng, dtype: datetime64[us]
'''