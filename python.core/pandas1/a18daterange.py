import pandas as pd
dr = pd.date_range('12/31/2010',periods=10,freq='ME')
print(dr)
'''
DatetimeIndex(['2010-12-31', '2011-01-31', '2011-02-28', '2011-03-31',
               '2011-04-30', '2011-05-31', '2011-06-30', '2011-07-31',
               '2011-08-31', '2011-09-30'],
              dtype='datetime64[us]', freq='ME')
'''