import socket

PORT = 9876

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind(("", PORT))
    print("[UDP] In ascolto...")
    data, addr = sock.recvfrom(1024)
    print("[UDP] Ricevuto:", data.decode())
