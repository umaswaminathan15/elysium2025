import json
jsn = json.load(open('tbler.json'))
print(jsn)
print(jsn['tbler'])
print(jsn['tbler'][0]['rno'])

'''
{'tbler': [{'rno': '1001', 'sname': 'x5', 'm1': '56.6', 'm2': '63'}, {'rno': '1001', 'sname': 'x3', 'm1': '45.5', 'm2': '43'}, {'rno': '1001', 'sname': 'x1', 'm1': '54.5', 'm2': '52'}]}
[{'rno': '1001', 'sname': 'x5', 'm1': '56.6', 'm2': '63'}, {'rno': '1001', 'sname': 'x3', 'm1': '45.5', 'm2': '43'}, {'rno': '1001', 'sname': 'x1', 'm1': '54.5', 'm2': '52'}]
1001
'''