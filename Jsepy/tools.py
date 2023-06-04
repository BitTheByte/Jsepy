import subprocess

class JsepyTools(object):
	@staticmethod
	def render(gui):
		# hardcoded string for now .. i need to change this
		subprocess.call(
			[
				'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe',
				f'--app={gui}',
			]
		)
