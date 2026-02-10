import socket 
import time   

HOST = "127.0.0.1"  
PORT = 6789        

# Crea un socket TCP (AF_INET=IPv4, SOCK_STREAM=TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    if client.connect_ex((HOST, PORT)) == 0:
        print("[CLIENT] Connesso al server")
    else:
        print("[CLIENT] Impossibile connettersi al server")
        print("[CLIENT] Assicurati che il server sia in esecuzione e che la porta sia corretta")
        print("[CLIENT] Uscita dal programma in 3 secondi")
        time.sleep(3)
        exit(1)
    while True:
        client.sendall(input("Inserisci il tuo messaggio: ").encode())  
        risposta = client.recv(1024).decode() 
        print("[CLIENT] Risposta:", risposta) 
        
        if risposta == "Server conferma: QUIT":
            print("[CLIENT] Chiusura connessione")
            time.sleep(3)
            break
