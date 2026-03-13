import pandas as pd
import numpy as np
ar = np.array(['O','r', 'a', 'n', 'g', 'e'])
sa = pd.Series(ar)
print(sa)
print()
print(sa[3])
'''
0    O
1    r
2    a
3    n
4    g
5    e
dtype: str

n
'''

