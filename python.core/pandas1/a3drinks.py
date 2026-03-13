import pandas as pd
L = [
    ['Coffee', 'Tea', 'Milk'],
    ['Pepsi', '7Up', 'Coke'],
    ['Orange', 'Mango', 'Grapes']
]
print(L)
df = pd.DataFrame(L)
print(df)
print(df[1])
'''
[['Coffee', 'Tea', 'Milk'], ['Pepsi', '7Up', 'Coke'], ['Orange', 'Mango', 'Grapes']]
        0      1       2
0  Coffee    Tea    Milk
1   Pepsi    7Up    Coke
2  Orange  Mango  Grapes
0      Tea
1      7Up
2    Mango
Name: 1, dtype: str
'''