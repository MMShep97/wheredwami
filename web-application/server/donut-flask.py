from whereami import predict
from whereami import predict_proba
from whereami.predict import predictfuk
import statistics
import ast
import operator
import time

from flask import Flask, jsonify
from flask_cors import CORS
from multiprocessing import Process, Manager, Value
from ctypes import c_char_p
import logging

#### VARIABLES #################################
posters = ["dupon", "fatalgas", "honeywell", "metaldus", "morton", "pascagoula", "pvcexplosion", "toxicrelease"]
distances = {"dupon": 77.5, "fatalgas": 51.75, "honeywell": 24.83, "metaldus": 20.167, "morton": 63.75, "pascagoula": 14.67, "pvcexplosion": 46, "toxicrelease": 32.5}
data = [[],[],[],[],[],[],[],[]]
od = False

##################################################

# Two values sent to Marco
postername = "default"
xcoord = -1.23
ycoord = 0

manager = Manager()
poster_name = manager.Value(c_char_p, 'gorf')
x_coord = Value('d', 1.23)
y_coord = Value('d', 0.0)

def get_x_coord(pred):
	global xcoord
	b = pred["pascagoula"]*distances["pascagoula"] + pred["metaldus"]*distances["metaldus"] + pred["honeywell"]*distances["honeywell"] + pred["toxicrelease"]*distances["toxicrelease"] + pred["pvcexplosion"]*distances["pvcexplosion"] + pred["fatalgas"]*distances["fatalgas"] + pred["morton"]*distances["morton"] + pred["dupon"]*distances["dupon"]
	xcoord = b
	return b

def get_predictions():
	global postername
	global xcoord
	global ycoord
	return postername, xcoord, ycoord

def predict_loop(poster_name, x_coord, y_coord):
    first = True
    chances_left = 4
    global postername
    global xcoord

    while (True):
        time.sleep(1)
        x = predictfuk()
        x = ast.literal_eval(x)
        print(x)
        postername = max(x.items(), key=operator.itemgetter(1))[0]
        poster_name.value = postername
        print("POSTERNAME: ", postername)

        od = False
        data = []

        if first or chances_left == 0:
            chances_left = 4
            prev_x = x
            # print(get_x_coord(x))
            first = False
            continue

        data.append(prev_x["dupon"] - x["dupon"])
        data.append(prev_x["fatalgas"] - x["fatalgas"])
        data.append(prev_x["honeywell"] - x["honeywell"])
        data.append(prev_x["metaldus"] - x["metaldus"])
        data.append(prev_x["morton"] - x["morton"])
        data.append(prev_x["pascagoula"] - x["pascagoula"])
        data.append(prev_x["pvcexplosion"] - x["pvcexplosion"])
        data.append(prev_x["toxicrelease"] - x["toxicrelease"])

        for i in range(len(data)):
            if data[i] >= 0.4 or data[i] <= -0.4:
                print("outlier detected", posters[i])
                od = True
                break
        if od:
            chances_left = chances_left - 1
            continue

        print("no outlier detected")
        prev_x = x
        print("x coord: ", get_x_coord(x))
        x_coord.value = get_x_coord(x)
        y_coord.value = 0


        #if poo == "s":
        #	for i in range(8):
        #		print(posters[i])
        #		print(round(statistics.stdev(data[i]),2), "     ", round(statistics.mean(data[i]),2))

        #print(predict_proba())

####### START OF SERVER #################################

DEBUG = True

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app= Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/active-poster', methods=['GET'])
def send_active_poster():
	return jsonify( {
		'name': poster_name.value,
		'xCoord': x_coord.value,
		'yCoord': y_coord.value
	})

if __name__ == '__main__':
    p = Process(target=predict_loop, args=(poster_name, x_coord, y_coord))
    p.start()
    app.run(host='0.0.0.0', port= 5000, use_reloader=False)
    p.join()
    print("IN MAIN: ", postername)

######## END OF SERVER #################################
