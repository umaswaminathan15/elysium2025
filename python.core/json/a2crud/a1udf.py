import json
def getData(jsnFile):
    try:
        return json.load(open(jsnFile))
    except:
        return {"tbler":[]}

def setData(data, jsnFile):
    try:
        fp = open(jsnFile, "w")
        json.dump(data, fp, indent=4)
        return True
    except:
        return False