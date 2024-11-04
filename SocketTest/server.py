import socket

server_address = ("0.0.0.0", 8000)

"""
Lager nettverkssocket med AF_INET, og bruker 
SOCK_STREAM for å definere bruk TCP protokoll, som holder oppe kommunikasjon,
istedenfor UDP, som kun sender og mottar beskjeder. 
"""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind(server_address) # Binder server-socketen til en ip-addresse og port

# Tar kun inn 5 koblinger samtidig
server.listen(5)

while True:
    # server.accept() returnerer en tuple for å håndtere connections
    # client-instansen kan vi bruke til å kommunisere med, addressen er kun addressen til klienten
    client, addr = server.accept()
    print(client.recv(1024).decode()) # Receiver max 1024 bytes fra client, decoder til ASCII og printer ut
    client.send('Hello from server'.encode()) # Sender melding fra server til klienten og encoder den