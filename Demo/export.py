from Jsepy.tools import JsepyTools
import glob
import os


def py_list_files(path):
	html = ""
	for file in glob.glob(path + "/*"):
		html += file + "<br>"
	return html

def py_run_calc():
	os.system('calc.exe')
	return 'done'

def new_window():
	JsepyTools.render('http://localhost:1337/view/other.html')
	return 'ok'