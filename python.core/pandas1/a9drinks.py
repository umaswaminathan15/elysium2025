import pandas as pd
d = {
     'hot':['Coffee', 'Tea', 'Milk'],
     'cool':['Pepsi', '7Up', 'Coke'],
     'soft':['Orange', 'Mango', 'Grapes']
}
print(d['cool'])
df = pd.DataFrame(d)
print(df['cool'])
'''
['Pepsi', '7Up', 'Coke']
0    Pepsi
1      7Up
2     Coke
Name: cool, dtype: str
'''