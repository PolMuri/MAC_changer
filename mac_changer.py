import subprocess
import re
import argparse

# Funció per canviar la direcció MAC d'una interfície de xarxa
def canviar_mac(interfície, nova_mac):
    print(f"Canviant la direcció MAC de {interfície} a {nova_mac}")

    # Desactiva la interfície
    subprocess.call(["sudo", "ifconfig", interfície, "down"])

    # Canvia la direcció MAC
    subprocess.call(["sudo", "ifconfig", interfície, "hw", "ether", nova_mac])

    # Activa la interfície
    subprocess.call(["sudo", "ifconfig", interfície, "up"])

# Funció per validar una direcció MAC
def validar_mac(mac):
    if not re.match(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", mac):
        return False
    return True

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--interficie", dest="interficie", help="Nom de la interfície de xarxa")
parser.add_argument("-m", "--mac", dest="nova_mac", help="Nova direcció MAC")
opcions = parser.parse_args()

if not opcions.interficie:
    opcions.interficie = input("Introdueix el nom de la interfície de xarxa: ")

if not opcions.nova_mac:
    opcions.nova_mac = input("Introdueix la nova direcció MAC: ")

if not validar_mac(opcions.nova_mac):
    print("La direcció MAC introduïda no és vàlida. Si us plau, utilitza el format XX:XX:XX:XX:XX:XX.")
else:
    canviar_mac(opcions.interficie, opcions.nova_mac)
    print("Direcció MAC canviada amb èxit!")
    resultat = subprocess.check_output(["ip", "a", "show", opcions.interficie]).decode()
    print("Estat de la interfície modificada:")
    print(resultat)


