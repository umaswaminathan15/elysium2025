import pandas as pd
dr = pd.date_range('12/31/2010',periods=10,freq='W')
print(dr)
'''
DatetimeIndex(['2011-01-02', '2011-01-09', '2011-01-16', '2011-01-23',
               '2011-01-30', '2011-02-06', '2011-02-13', '2011-02-20',
               '2011-02-27', '2011-03-06'],
              dtype='datetime64[us]', freq='W-SUN')
'''