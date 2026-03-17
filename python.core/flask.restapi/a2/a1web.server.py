from flask import Flask,request,jsonify
app = Flask('erRestAPI')
rows = []
@app.route('/er', methods=['POST'])
def addData():
    newRow = request.json
    rows.append(newRow)
    return (jsonify(newRow), 201)
@app.route('/er', methods=['GET'])
def getData():
    return jsonify(rows)
@app.route('/er/<int:rno>', methods=['GET'])
def findData(rno):
    for row in rows:
        print(row["rno"])
        if row["rno"] == rno:
            return jsonify(row)
    return (jsonify({"error": f"{rno} not found"}), 404)
@app.route('/er/<int:rno>', methods=['PUT'])
def updateData(rno):
    for row in rows:
        if row["rno"] == rno:
            editData = request.json
            row.update(editData)
            return jsonify(row)
    return (jsonify({"error": f"{rno} not found"}), 404)
@app.route('/er/<int:rno>', methods=['DELETE'])
def deleteData(rno):
    global rows
    r = []
    for row in rows:
        if row["rno"] != rno:
            r.append(row)
    if len(r) < len(rows):
        rows = r
        return jsonify({'message':f"{rno} deleted"})
print("RESTAPI URL: http://127.0.0.1:1234")
app.run(debug=True, host='0.0.0.0', port=1234)
