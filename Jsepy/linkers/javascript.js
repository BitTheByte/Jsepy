var endpoint = '/api/python/'



var script = document.createElement("script"); 
script.src = 'https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js'; 
document.head.appendChild(script);



function Python(options) {

	var PyFunction  = options.fn;
	var PyArguments	= "";
	var PyAPIPath   = "";
	var JsCallBack  = options.callback;

	if (typeof options.args !== 'undefined'){
		for (var i=0; i < options.args.length; i++)
			PyArguments += "/" + encodeURIComponent(options.args[i]);
	}



	if (PyArguments.length > 0){
		PyAPIPath = endpoint + PyFunction + PyArguments
	}else{
		PyAPIPath = endpoint + PyFunction
	}

	$.get({
		type:'GET',
		url: PyAPIPath,
		success:JsCallBack
	})
}
