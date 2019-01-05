from Jsepy.app import Jsepy


jspy = Jsepy(
		base='Demo',      # folder which contain html files
		pybase='Demo',    # folder which contain python linker file
		pylink='export',  # python linker file name 
		host='localhost', # Host to run the server on    
		port=1337         # connection port   
	)



jspy.start_server()      # Loading server 
jspy.render('main.html') # Main page

