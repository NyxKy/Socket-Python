import socket

HOST = "127.0.0.1"
PORT = 9876

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    msg = "Ciao UDP Server"
    sock.sendto(msg.encode(), (HOST, PORT))
    print(f"[UDP] Inviato: {msg}")
