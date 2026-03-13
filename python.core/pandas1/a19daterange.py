import pandas as pd
dr = pd.date_range('12/31/2010',periods=10,freq='YE')
print(dr)

'''
DatetimeIndex(['2010-12-31', '2011-12-31', '2012-12-31', '2013-12-31',
               '2014-12-31', '2015-12-31', '2016-12-31', '2017-12-31',
               '2018-12-31', '2019-12-31'],
              dtype='datetime64[us]', freq='YE-DEC')
'''
