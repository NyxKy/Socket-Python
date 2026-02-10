import socket

HOST = "127.0.0.1"
PORT = 6789

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(b"Ciao Server")
    risposta = client.recv(1024).decode()
    print("[CLIENT] Risposta:", risposta)
