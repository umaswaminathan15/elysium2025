import pandas as pd
d = {
     'hot':['Coffee', 'Tea', 'Milk'],
     'cool':['Pepsi', '7Up', 'Coke'],
     'soft':['Orange', 'Mango', 'Grapes']
}
print(d['cool'][1])
df = pd.DataFrame(d)
print(df['cool'][1])
'''
7Up
7Up
'''