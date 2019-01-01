var endpoint = "http://localhost:5000/api/py/"


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


/*
function PY(){

	var PyFuncName  = 	arguments[0]
	var PyArguments	=	"";
	var PyAPIPath	=	"";

	for (var i=1; i < arguments.length; i++){
		PyArguments += "/" + encodeURIComponent(arguments[i]);
	}

	if (PyArguments.length > 0){
		PyAPIPath = endpoint + PyFuncName + PyArguments
	}else{
		PyAPIPath = endpoint + PyFuncName
	}


	return PyAPIPath;
}


function CALL(uri,fn)
{
	$.get({
		type:'GET',
		url: uri,
		success:fn
	})
}*/