import socket  
import time    

HOST = "127.0.0.1"  
PORT = 6789       

# Crea un socket TCP (AF_INET=IPv4, SOCK_STREAM=TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT)) 
    server.listen()         
    print("[SERVER] In ascolto...") 
    conn, addr = server.accept()  
    with conn:  
        print("[SERVER] Client:", addr) 
        while True:
            data = conn.recv(1024).decode()  
            print("[SERVER] Ricevuto:", data)  
                
            risposta = "Server conferma: " + data.upper()  
            conn.sendall(risposta.encode()) 
            
            if data == "quit":
                print("[SERVER] Chiusura connessione richiesta dal client")
                time.sleep(3)
                break
