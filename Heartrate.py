from crypt import methods
from flask import Flask, jsonify, request
app = Flask(__name__)

heartrates = [
    {
        "heart_id" : "1",
        "date" : "01/10/2022",
        "heart_rate" : "144 bpm"
    },
    {
        "heart_id" : "2",
        "date" : "01/10/2022",
        "heart_rate" : "160 bpm"
    }
]

@app.route ('/heartrates', methods=['GET'])
def getHeartrates():
    return jsonify(heartrates)

@app.route('/heartrates', methods=['POST'])
def addHeartrates():
    heartrate = request.get_json()
    heartrates.append(heartrate)
    return {'id':len(heartrates)} , 200

@app.route('/heartrates/<int:index>', methods=['DELETE'])
def deleteHeartrates(index):
    heartrates.pop(index)
    return 'Heart rate information was successfully deleted', 200

if __name__ == '__main__':
    app.run()