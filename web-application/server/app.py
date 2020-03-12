from flask import Flask, jsonify
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/active-poster', methods=['GET'])
def ping_pong():
    return jsonify( {
        'name': 'pascagoula',
        'xCoord': '23',
        'yCoord': '25',
    })


if __name__ == '__main__':
    app.run()