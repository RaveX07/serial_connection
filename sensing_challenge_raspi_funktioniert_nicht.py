from sr.robot3 import Robot, INPUT, OUTPUT, Colour, LED_A, LED_B, LED_C, Note
import random

RUGGEDUINO = "75230313833351613121"

robot = Robot(
    ignored_arduinos=[RUGGEDUINO],
    raw_ports=[(RUGGEDUINO, 115200)],
    debug = True, wait_for_start=False
)

def serial_send_string(string_to_send: str):
    string_with_endln = f"{string_to_send}\n"                   # Hinzufügen von Zeilenumbruch (Signalisiert ende der Nachricht)
    bytes_object = string_with_endln.encode()                   # Umwandeln von string zu bytes
    robot.raw_serial_devices[RUGGEDUINO].write(bytes_object)    # Senden der Nachricht

robot.kch.leds[LED_A].colour = Colour.RED
serial_send_string("a")     # Beispiel-Nachricht
robot.kch.leds[LED_A].colour = Colour.GREEN