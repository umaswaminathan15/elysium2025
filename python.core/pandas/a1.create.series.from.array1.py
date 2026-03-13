import pandas as pd
import numpy as np
Lst = ['Sun','Mon','Tue','Wed']
ar = np.array(Lst)
sr = pd.Series(ar)
print(Lst)
print(ar)
print(sr)
'''
['Sun', 'Mon', 'Tue', 'Wed']
['Sun' 'Mon' 'Tue' 'Wed']
0    Sun
1    Mon
2    Tue
3    Wed
dtype: str
'''