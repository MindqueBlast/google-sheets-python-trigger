from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    arg1 = int(data.get("arg1", 0))
    arg2 = int(data.get("arg2", 0))
    row = data.get("row")

    result = arg1 + arg2
    print(f"Row {row}: {arg1} + {arg2} = {result}")

    # <-- RETURN sum along with status
    return jsonify({
        "status": "complete",
        "sum": result
    })
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

