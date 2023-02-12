# Microservice for Outlook

# Communication Contract
A. Clear instructions for how to REQUEST data from the microservice you implemented. Include an example call.

The microservice uses sockets implemented with python's socket module in order to communicate with the client program. 
In order to request data, the microservice (server.py) should be running locally and using localhost as the host and any port within 
the range 1024-65535. The host and port must be the same from the client program. Once the microservice is running, the client
can create a socket object that connects to the server.

Once the connection has been established the client can send a message to the server.
The message should be in json format.

If a "save" request is being made then the json text should be in the following format:

{ "action" : "save", "path" : "name_of_file_to_save.txt", "info" : "financial information to be saved" }

If a "load" request is being made then the json text should be in the following format:

{ "action" : "load", "path" : "name_of_file_to_upload_from.txt" }

The socket will then send this information as bytes, encoded in utf-8 to be recieved by the microservice. The message cannot
be longer than 1024 bytes. 

Example Call: User wants to save "You have 1 million dollars" to the file outlook.txt

````
client_info =  {"action": "save", "path": "outlook.txt", "info": "You have 1 million dollars"}

client_info_json = json.dumps(client_info)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((127.0.0.1, 54290)) #connects to the server at the host/port
    s.sendall(bytes(client_info_json, encoding="utf-8"))
````
