import socket

HOST = "127.0.0.1"
PORT = 6789

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print("[SERVER] In ascolto...")
    conn, addr = server.accept()
    with conn:
        print("[SERVER] Client:", addr)
        data = conn.recv(1024).decode()
        print("[SERVER] Ricevuto:", data)
        risposta = "Server conferma: " + data.upper()
        conn.sendall(risposta.encode())
