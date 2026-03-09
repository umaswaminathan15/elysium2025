import json
jsn = json.load(open('tbler.json'))
rows = jsn['tbler']
for row in rows:
    print(row)

'''
{'rno': '1001', 'sname': 'x5', 'm1': '56.6', 'm2': '63'}
{'rno': '1001', 'sname': 'x3', 'm1': '45.5', 'm2': '43'}
{'rno': '1001', 'sname': 'x1', 'm1': '54.5', 'm2': '52'}

'''