import jsonpickle
from flask import Flask, request
from datetime import date
import os
import signal

app = Flask(__name__)

@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'

@app.route('/users/<user_id>', methods=['GET','POST','PUT','DELETE'])
def user(user_id):
    if request.method == 'GET':
        return {"status": "ok", "user_name": "HODAYA"}, 200
    return {"Hi, this is for test"}, 200





app.run(host='0.0.0.0', debug=True, port=5000)