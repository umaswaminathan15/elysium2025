import pandas as pd
dr = pd.DataFrame()
dr['rng'] = pd.date_range('12/31/2010',periods=10)
print(dr[:3])
print(dr.head(3))
print(dr[7:])
print(dr.tail(3))
'''
         rng
0 2010-12-31
1 2011-01-01
2 2011-01-02
         rng
0 2010-12-31
1 2011-01-01
2 2011-01-02
         rng
7 2011-01-07
8 2011-01-08
9 2011-01-09
         rng
7 2011-01-07
8 2011-01-08
9 2011-01-09
'''