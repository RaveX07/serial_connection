from connection_raspi import Serial_Manager     # Importieren von Serial Manager Klasse
import random

serial = Serial_Manager()       # Initialisieren von Serial_Manager

if random.randint(0, 1) == 0:   # Beispiel-Logik 
    serial.send_string("0")     # Beispiel-Nachricht
else:
    serial.send_string("1")     # Beispiel-Nachricht