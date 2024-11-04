import socket, threading
from colorama import Fore, Back, Style

server_address = ('0.0.0.0', 8000)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Internett-socket, TCP-protokoll
server.bind(server_address) 
server.listen() # Venter på incoming connections

clients = []
nicknames = []

def broadcast(message): # Sender message til alle clients i clients-lista for å broadcaste
    for client in clients:
        client.send(message)

def handle(client): # Håndterer client-connection, henter inn melding prosserer og 
    while True:
        try: # Prøv å hendte melding fra client
            message = client.recv(1024)
            broadcast(message)

        except: # Hvis det ikke funker, kutt connection fra clienten, terminater loopen
            index = clients.index(client) # Får ut indeksen til client
            clients.remove(client) # Fjerner client fra lista
            client.close() # Lukker     connection
            nickname = nicknames[index] # Henter ut nickname
            nicknames.remove(nickname) # Fjerner nickname fra oversikten

            broadcast((Fore.RED + f'{nickname} closed connection.' + Style.RESET_ALL).encode('utf-8'))
            break

def receive():
    while True:
        client, addr = server.accept() # Kjører konstant accept method for å returnere client og addresse
        print(Fore.GREEN + f"Connected with {addr}" + Style.RESET_ALL)
        client.send('NICK'.encode('utf-8')) # Sender et codeword som kun klienten ser, får beskjed om å sende inn nickname
        nickname = client.recv(1024).decode('utf-8') # Decoder max 1024 bytes til navnet

        nicknames.append(nickname) # Legger til nickname i lista som har samme indeks som klient-instansen
        clients.append(client) # Legger til klient-instans

        print(f'Nickname of the client is {nickname}.') # Gir info til serveren om klient-connection og nickname
        client.send((Fore.GREEN + 'Connected to the server.\n' + Style.RESET_ALL).encode('utf-8'))
        broadcast((Fore.YELLOW + f'{nickname} has joined the chat!' + Style.RESET_ALL).encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,)) # Må prosserere alle koblinger samtidig, bruker dermed en thread
        thread.start() # Starter opp threaden

print("Server is listening for clients...")
receive() # Kaller på main-funksjonen receive