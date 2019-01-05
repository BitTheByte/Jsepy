from .linkers.python import handler
from .tools import JsepyTools
from threading import Thread
from flask import Flask
import sys
import os


class helpers(object):
	def read_file(self,path):
		try:
			return open(path,'r').read()
		except Exception as e:
			return e

class routes(helpers):

	def api(self):
		return ('{"python":"%s"})' % self.api_path)

	def python(self,path): 
		return handler(
				self.pylinker,
				path,
				self.api_path
			)

	def window_handler(self,window):
		return self.read_file(
			'{base}/{window}'.format(
					base=self.base,
					window=window
				)
			)

	def linker(self): 
		return self.read_file(
				'%s\\linkers\\javascript.js' % os.path.abspath(os.path.dirname(__file__))
			)


class Jsepy(routes):
	app = Flask(__name__)


	def __init_imports__(self):
		sys.path.insert(0, self.pybase)
		self.pylinker = __import__(self.pylink)


	def __init__(self,
			base='.',
			pybase='.',
			pylink='.',
			port=1337,
			host='localhost',
			scheme = 'http'
		):

		self.host 		= host
		self.port 		= port
		self.base 		= base
		self.pylink 	= pylink
		self.pybase 	= pybase
		self.scheme 	= scheme
		self.api_path 	= '/api/python'
		self.veiw_path 	= '/view'

		self.__init_imports__()



	def __init_server(self):
		self.app.run(host=self.host,port=self.port,debug=True,use_reloader=False)

	def start_server(self):
		
		self.app.route('{}/<path:path>'.format(self.api_path))(self.python)
		self.app.route('{}/<window>'.format(self.veiw_path))(self.window_handler)
		self.app.route('/fapi')(self.api)
		self.app.route('/japi')(self.linker)

		Thread(target=self.__init_server).start()


	def render(self,gui):
		JsepyTools.render('{scheme}://{host}:{port}{veiw_path}/{gui}'.format(
			scheme=self.scheme,
			host=self.host,
			port=self.port,
			veiw_path=self.veiw_path,
			gui=gui
		))




