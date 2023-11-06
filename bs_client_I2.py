import socket
from sys import exit

anwser=input("Que veux-tu envoyer au serveur : ")
# On définit la destination de la connexion
host = '10.1.4.2'  # IP du serveur
port = 13337       # Port choisir par le serveur

# Création de l'objet socket de type TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
try:
    s.connect((host, port))
    print(f"Connecté avec succès au serveur {host} sur le port {port}")
except:
    print("Erreurs lors de la connexion au serveur")
    exit(1)

s.sendall(anwser.encode())

# On reçoit 1024 bytes qui contiennent peut-être une réponse du serveur
data = s.recv(1024)

# On libère le socket TCP
s.close()

# Affichage de la réponse reçue du serveur
print(f"Le serveur a répondu {repr(data)}")
exit(0)