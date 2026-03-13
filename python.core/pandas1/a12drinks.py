import pandas as pd
d = {
     'hot':['Coffee', 'Tea', 'Milk'],
     'cool':['Pepsi', '7Up', 'Coke'],
     'soft':['Orange', 'Mango', 'Grapes']
}
df = pd.DataFrame(d,index=['row1','row2','row3'])
print(df)
'''
         hot   cool    soft
row1  Coffee  Pepsi  Orange
row2     Tea    7Up   Mango
row3    Milk   Coke  Grapes
'''