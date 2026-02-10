import socket 
import time  

HOST = "127.0.0.1"  
PORT = 9876       

# Crea un socket UDP (AF_INET=IPv4, SOCK_DGRAM=UDP)
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    while True: 
        msg = input("Inserisci il tuo messaggio: ")  

        sock.sendto(msg.encode(), (HOST, PORT)) 
        print(f"[UDP] Inviato: {msg}")  

        if msg == "quit":
            print("[UDP] Chiusura connessione")
            time.sleep(3)
            break
