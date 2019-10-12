import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 3306
print('Listening for connections from host: ', socket.gethostbyname(socket.gethostname()))

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        # Setup the port and get it ready for listening for connections
        s.bind((HOST, PORT))
        s.listen(1)
        print('Waiting for incoming connections...')
        conn, addr = s.accept()  # Wait for incoming connections
        conn.sendall('Connected to the python server!'.encode('utf-8'))
        print('Connected to: ', addr)
