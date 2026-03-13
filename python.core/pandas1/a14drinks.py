import pandas as pd
d = {
     'hot':['Coffee', 'Tea', 'Milk'],
     'cool':['Pepsi', '7Up', 'Coke'],
     'soft':['Orange', 'Mango', 'Grapes']
}
df = pd.DataFrame(d)
print(df.loc[1])
df = pd.DataFrame(d,index=['row1','row2','row3'])
print(df.loc['row2'])
'''
hot       Tea
cool      7Up
soft    Mango
Name: 1, dtype: str
hot       Tea
cool      7Up
soft    Mango
Name: row2, dtype: str
'''
