import socket
#Simulation of a vulnerable service
host = '127.0.0.1'  # Localhost for testing
port = 21 # FTP port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))
server_socket.listen(1)
print(f"Listening on {host}:{port}...")
while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr} has been established!")
    client_socket.sendall(b"220 Fake FTP Service\r\n")
    client_socket.close()