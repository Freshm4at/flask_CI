from flask import Flask
from redis import Redis, RedisError
import os
import socket

redis = Redis(host = "redis-server",db=0,socket_timeout=2,socket_connect_timeout=10)
app = Flask(__name__)
@app.route("/")
def index():
	return "<h1> hello world </h1>
	
@app.route("/visit")
def visit_counting():
	try:
		visits = redis.incr("counter")
	except:
		visits = "<i> I cannot connect to redis i don't know why </i>"
	html = "<h1Numver of visits : {}<h1>, \n Hostname {}".format(visits,socket.gethostname())
	
	
if __name__ == "__main__":
	app.run(debug = True,port =80, host = '0.0.0.0')