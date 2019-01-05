def handler(module,path,api_path):
	target  = path.replace(api_path,"").split("/")
	fn,args = target[0],target[1::]
	fn = getattr(module, fn,None)
	if fn:
		try:
			response = fn() if not args else fn(*args)
		except Exception as e:
			response = str(e)
		return response
	return "Undefined function"
