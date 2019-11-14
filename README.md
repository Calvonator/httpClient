# httpClient
Basic Python HTTP client using Socket, http.client and URLLIB modules to create HTTP connections - with optional choice to connect through a burp suite proxy. 

--Menu Options--

Type in either HTTP[proxy], Socket[proxy] or URLLIB[proxy] where [proxy] will send the connection through a burp suite proxy or 'q' to quit the program.

--To-Do List--
  - Implement proxy functionality with URLLIB module connection
  - mySocket and mySocketProxy functions are assigning a time value to the 'z' variable twice
  - Look for **improvements/extra functionality** to add to the program
	- The program currently can't handle HTTP Response code 301 Moved Permanently. The response contains the URI to the resources new             location. https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/301
	- Current setup does not allow for the importing of individual functions as the while loop is imported into the importing script. 	    Upload a version of the script not containing the loop to allow for individual importing of functions.
