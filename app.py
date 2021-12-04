from flask import Flask
import time
from flask.json import jsonify
from flask import request
app = Flask(__name__)

cache = {'time':time.gmtime(time.time()),'ip': "-"}


@app.route("/json")
def getGson():
    return cache

@app.route("/create")
def create():
    cache['time'] = 0
    return jsonify(cache['time'])

@app.route("/time")
def increment():
    cache['time'] = time.gmtime(time.time())
    cache['ip'] = request.remote_addr
    return ""

@app.route("/")
def read():
    t = cache['time']
    ip = cache['ip']
    return "Время {}:{} <br> {}.{}.{} \n <br><br> Ip: {}".format(t[3] + 3,t[4],t[2],t[1],t[0], ip)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
