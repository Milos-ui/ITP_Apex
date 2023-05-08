from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/data', methods=['GET'])
def get_data():
    data = {
        'message': 'Hallo von Flask!'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run()
