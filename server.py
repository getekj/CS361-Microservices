
import socket
import json

HOST = "127.0.0.1" # local host
PORT = 54290       # Port to listen on

# creates a socket object and since using "with" don't have to call s.close()
# AF_INET is the internet address for IPv4, SOCK_STREAM is the socket type for TCP protocol
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) #bind associates the socket with the specific network and port number
    s.listen() #listen enables the server to accept connections, makes a listening socket
    conn, addr = s.accept() #accept blocks execution and waits for incoming client connection, returns a new socket
    #object representing the connection and addr a tuple containing host and port
    # conn is the new socket object that used to comm w/ client
    with conn:
        # accepted 2 way handshake
        print(f"Connected by {addr}")
        # sending and receiving messages with client
        while True:
            data = conn.recv(1024) #reads what ever the client sends, if data is an empty object that signals the ct closed the connection
            if not data: #empty obj sent from ct means connection is closed so we exit loop
                break
            #if data == b"Save":
            data = data.decode("utf-8")
            data = json.loads(data)
            print(f"recieved the msg: {format(data)}")
            print(type(data))
            if data["action"] == "save":
                print("save file")
                with open(data["path"], 'w') as info_file:
                    info_file.write(data["info"])
                success_msg = {"status":"Success"}
                success_msg_json = json.dumps(success_msg)
                conn.sendall(bytes(success_msg_json,encoding="utf-8"))
            elif data["action"] == "load":
                print("load file")
                send_back = {}
                with open(data["path"], 'r') as load_file:
                    #print(load_file.read())
                    #send_back_text = load_file.read()
                    send_back["info"] = load_file.read()
                print(send_back)
                send_back_json = json.dumps(send_back)
                conn.sendall(bytes(send_back_json, encoding="utf-8"))
            else:
                fail_message = {"status": "Failure"}
                fail_msg_json = json.dumps(fail_message)
                conn.sendall(bytes(fail_msg_json, encoding="utf-8"))


