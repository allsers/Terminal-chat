import socket, threading
from colorama import Fore, Back, Style
from pick import pick

def format(text: str, color: str) -> str:
    if color == "Blue":
        color = Fore.BLUE 
    elif color == "Red":
        color = Fore.RED
    elif color == "Green":
        color = Fore.GREEN
    elif color == "Yellow":
        color = Fore.YELLOW

    return color + text + Style.RESET_ALL

ERASE_LINE_ABOVE = "\033[1A\033[2K"

nickname = input("Enter your nickname:\n")

title = "Choose color for name tag: "
options = ["Blue","Red","Green","Yellow"]
color, _ = pick(options, title, multiselect=False, min_selection_count=1)


address = ("192.168.1.12", 8000)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Oppretter en socket med samme argumenter
client.connect(address) # Connecter client til server på samme port

def receive(): # En av to metoder som henter inn melding fra server
    while True:
        try:
            message = client.recv(1024).decode('utf-8') # Receiver fra server, der serveren bruker et client-instants for å sende
            if message == "NICK":
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        
        except: # Kan ikke koble til serveren, server ikke oppe
            print(Fore.RED + "An error occurred!" + Style.RESET_ALL)
            client.close()
            break

def write(): # En av to metoder som sender melding til server
    while True:
        text = input("")
        print(ERASE_LINE_ABOVE, end='')
        if text:
            message = f'{format(nickname + ':', color)} {text}'
            client.send(message.encode('utf-8'))

# Kjører både receive-thread og write-thread:
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()