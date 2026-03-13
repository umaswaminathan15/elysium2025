import pandas as pd
L = [
    ['Coffee', 'Tea', 'Milk'],
    ['Pepsi', '7Up', 'Coke'],
    ['Orange', 'Mango', 'Grapes']
]
df = pd.DataFrame(L,index=['hot', 'cool', 'soft'])
print(df)
'''
           0      1       2
hot   Coffee    Tea    Milk
cool   Pepsi    7Up    Coke
soft  Orange  Mango  Grapes

'''