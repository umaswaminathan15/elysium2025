import pandas as pd
L = [
    ['Coffee', 'Tea', 'Milk'],
    ['Pepsi', '7Up', 'Coke'],
    ['Orange', 'Mango', 'Grapes']
]
df = pd.DataFrame(L,index=['hot', 'cool', 'soft'])
print(df[1][1])
print(df[1]['cool'])

'''
7Up
'''
