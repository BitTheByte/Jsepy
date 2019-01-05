# Jsepy
Jsepy is hybrid GUI framwork using python as backend and HTML/JS/CSS as frontend gui.   
**This framework isn't ready for production it's still in development**

# App route
```
  App : Demo app using Jsepy
    |-> main.html : Main gui window
    |-> other.html : Html window
    |-> export.py : Python code accessable from the linker 

  Jsepy : Main library folder
    |-> app.py : Jsepy code
    |-> tools.py : Rendering code
    |-> linkers/  : Files to provide communication between js and python
 ```
 # Javascript api (For now)
```javascript
Python({
	fn:'Python function name', //Required
	args: [1,2,3,4,5],         //Optional
	callback:function(res){    //Optional

	}
})
```

# Demo app
![](Assets/main.png)

