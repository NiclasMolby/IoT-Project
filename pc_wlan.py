import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = ""          # Get local machine name
port = 4007                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.listen()                          # Now wait for client connection.
while True:
    c, addr = s.accept()        # Establish connection with client.
    print('Got connection from', addr)
    print(c.recv(1024))
    c.send('Hi from server!'.encode())
    c.close()  
    s.close()
    break
