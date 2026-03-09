import json
jsn =json.load(open('tbler.json'))
rows = jsn['tbler']
for row in rows:
    for col in row.values():
        print(f"{col:<10}", end=" ")
    else:
        print()

'''
1001       x5         56.6       63         
1001       x3         45.5       43         
1001       x1         54.5       52    
'''