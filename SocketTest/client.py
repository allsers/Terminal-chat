import socket
address = ("127.0.0.1", 8000)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Oppretter en socket med samme argumenter
client.connect(address) # Connecter client til server på samme port

client.send('Hello from client'.encode()) # Sender melding
print(client.recv(1024).decode())