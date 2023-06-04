from Jsepy.tools import JsepyTools
import glob
import os


def py_list_files(path):
	return "".join(f"{file}<br>" for file in glob.glob(f"{path}/*"))

def py_run_calc():
	os.system('calc.exe')
	return 'done'

def new_window():
	JsepyTools.render('http://localhost:1337/view/other.html')
	return 'ok'