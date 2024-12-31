import serial
from time import sleep

class Serial_Manager():
    def __init__(self, port="/dev/ttyACM0", baud_rate=115200):
        self.port = port                # Port vom Arduino (muss WAHRSCHEINLICH nicht geändert werden)
        self.baud_rate = baud_rate      # Baudrate (muss bei Pi und Arduino gleich sein) --> Standard 115200
        
        # Initialisierung von serieller Verbindung
        self.serial_connection = serial.Serial(port, baud_rate, timeout=3)
        self.serial_connection.setDTR(False)
        sleep(1)
        self.serial_connection.flushInput()
        self.serial_connection.setDTR(True)
        sleep(2)

    def send_string(self, string_to_send: str):
        string_with_endln = f"{string_to_send}\n"           # Hinzufügen von Zeilenumbruch (Signalisiert ende der Nachricht)
        string_as_bytes = str.encode(string_with_endln)     # Umwandeln von string zu bytes
        self.serial_connection.write(string_as_bytes)       # Senden der Nachricht
        
        
if __name__ == "__main__":
    serial_manager = Serial_Manager()                       # Erzeugen von Serial_Manager Klasse
    
    serial_manager.send_string("Hello World")               # Beispielnachricht