import socket  
import time    

PORT = 9876  

# Crea un socket UDP (AF_INET=IPv4, SOCK_DGRAM=UDP)
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind(("", PORT)) 
    print("[UDP] In ascolto...") 
    
    while True:
        data, addr = sock.recvfrom(1024)  
        print("[UDP] Ricevuto:", data.decode()) 
        
        if data.decode() == "quit":
            print("[UDP] Chiusura connessione richiesta dal sender")
            time.sleep(3)
            break
