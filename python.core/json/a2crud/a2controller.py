from a1udf import *
def createData(newData):
    try:
        oldData = getData('tbler.json')
        oldData['tbler'].append(newData)
        setData(oldData, 'tbler.json')
        return True
    except:
        return False
def readDatas():
    try:
        data = getData('tbler.json')
        if not data['tbler']:
            return False
        elif len(data['tbler']) <=0:
            return False
        row = data['tbler'][0]
        for col in row.keys():
            print(f"{col : <10}", end='')
        else:
            print(f"{'total': <10}", end='')
            print(f"{'average': <10}", end='')
            print(f"{'result': <10}", end='')
            print()
        rows = data['tbler']
        for row in rows:
            row['total']=row['m1'] + row['m2']
            row['average']=row['total']/2
            row['result']='pass' if row['m1'] > 34.4 and row['m2'] > 34.4 else 'fail'
            cols = row.values()
            for col in cols:
                print(f"{col : <10}", end='')
            else:
                print()
    except:
        print("no data")
        return
def readData(rno):
    try:
        data = getData('tbler.json')
        if not data['tbler']:
            return False
        elif len(data['tbler']) <=0:
            return False
        row = data['tbler'][0]
        for col in row.keys():
            print(f"{col : <10}", end='')
        else:
            print(f"{'total': <10}", end='')
            print(f"{'average': <10}", end='')
            print(f"{'result': <10}", end='')
            print()
        rows = data['tbler']
        for row in rows:
            if row['rno'] == rno:
                row['total']=row['m1'] + row['m2']
                row['average']=row['total']/2
                row['result']='pass' if row['m1'] > 34.4 else 'fail'
                cols = row.values()
                for col in cols:
                    print(f"{col : <10}", end='')
                else:
                    print()
                break
    except:
        print("no data")
        return
def updateData(rno, editData):
    data = getData('tbler.json')
    rows = data['tbler']
    for row in rows:
        if row['rno'] == rno:
            for key, value in editData.items():
                if key in row:
                    row[key] = value
            setData(data, 'tbler.json')
            print(f"updated {rno} data")
            return True
        print(f"{rno} data not found")
        return False
def deleteData(rno):
    oldData = getData('tbler.json')
    rows = oldData['tbler']
    newData = []
    for row in rows:
        if row['rno'] != rno:
            newData.append(row)
    if len(newData) < len(rows):
        newData = {"tbler" : newData}
        setData(newData, 'tbler.json')
        print(f"erased {rno} data")
        return True
    else:
        print(f"{rno} data not found")
        return False


