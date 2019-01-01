from linkers.python import handler
from helpers.dev import *
from flask import Flask
import sys

app = Flask(__name__)

# ==================== Jsepy routes ========================= #
@app.route('/api/py/<path:path>')
def python(path): 
	sys.path.insert(0, config.USR_PATH)
	return handler(__import__(config.EXPORT),path)

@app.route('/japi')
def jsapi(): return send_file("linkers/javascript.js")

@app.after_request
def headers(response): return allow_cors(response)
# ==================== Jsepy routes ========================= #


@app.route('/')
def main(): return send_file(config.GUI)


run_server(app)