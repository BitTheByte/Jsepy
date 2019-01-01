from webview import create_window
from threading import Thread
import config


import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


def run_server(app):
	def start():
		app.run(debug=False, use_reloader=False)
	Thread(target=start).start()
	create_window(config.WIN_NAME,'http://localhost:5000')

def send_file(path):
	return open(path,'r').read()

def allow_cors(res):
  res.headers.add('Access-Control-Allow-Origin', '*')
  return res