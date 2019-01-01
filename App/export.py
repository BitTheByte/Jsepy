import os
import glob
def py_list_files(path):
	html = ""
	for file in glob.glob(path + "/*"):
		html += file + "<br>"
	return html

def py_run_calc():
	os.system('calc.exe')
	return 'done'
