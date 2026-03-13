import pandas as pd
dr = pd.date_range('12/31/2010',periods=10)
print(dr)
'''
DatetimeIndex(['2010-12-31', '2011-01-01', '2011-01-02', '2011-01-03',
               '2011-01-04', '2011-01-05', '2011-01-06', '2011-01-07',
               '2011-01-08', '2011-01-09'],
              dtype='datetime64[us]', freq='D')
'''