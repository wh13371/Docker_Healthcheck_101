#! /usr/bin/env python

import sys, time, os, datetime, json, socket, threading

from flask import Flask, Response, render_template, jsonify # pip install flask

app = Flask(__name__)
FLASK_APP_PORT = os.getenv('FLASK_APP_PORT', 46664)
APP_NAME="flask101"
__version__ = "23.09.2020"

def get_now():
	return datetime.datetime.now().strftime("%Y:%m:%d %H:%M:%S.%f")

def get_now_iso():
    return datetime.datetime.utcnow().isoformat()

def get_epoch():
	return time.time()

def get_epoch_ns():
	return time.time_ns()

def get_pid():
	return os.getpid()

def get_hostname():
	return socket.gethostname()

def get_appname():
	return APP_NAME

def get_app_uptime():
    secs = get_epoch() - app_start_time
    result = datetime.timedelta(seconds=secs)
    return str(result)

def dd(message, level="INFO", **kwargs):
	log = {'timestamp': get_now(), 'epoch': get_epoch(), 'pid': get_pid(), 'level': level, 'message': message}
	if kwargs: log['kwargs'] = json.dumps(kwargs)
	print(log)
	sys.stdout.flush()
	return log

#

app_start_time = get_epoch()

@app.route("/")
def index():
	data = {
		'hostname': get_hostname(),
		'app-name': get_appname(),
		'app-start-time': app_start_time,
		'app-uptime': get_app_uptime(),
		'request-ts-nano': get_epoch_ns(),
		'request-ts-human': get_now(),
		'version': __version__,
	}
	dd(data, "DEBUG", route="/")
	return jsonify(data), 200


if __name__ == '__main__':
	dd("Starting Flask")
	app.run(host='0.0.0.0', port=FLASK_APP_PORT, debug=False)
