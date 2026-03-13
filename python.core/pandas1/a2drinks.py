import pandas as pd
drinks = ['hot', 'cool', 'soft']
print(drinks)
df = pd.DataFrame(drinks)
print(df)
print(df[0][1])
'''
['hot', 'cool', 'soft']
      0
0   hot
1  cool
2  soft
cool
'''