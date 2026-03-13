import pandas as pd
d = {
     'hot':['Coffee', 'Tea', 'Milk'],
     'cool':['Pepsi', '7Up', 'Coke'],
     'soft':['Orange', 'Mango', 'Grapes']
}
print(d)
df = pd.DataFrame(d)
print(df)
'''
{'hot': ['Coffee', 'Tea', 'Milk'], 'cool': ['Pepsi', '7Up', 'Coke'], 'soft': ['Orange', 'Mango', 'Grapes']}
      hot   cool    soft
0  Coffee  Pepsi  Orange
1     Tea    7Up   Mango
2    Milk   Coke  Grapes
'''