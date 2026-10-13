from microbit import *
import random

# Muestra una figura según el número elegido al azar.
def jugar():
    resultado = random.randint(0, 2)

    if resultado == 0:
        # Piedra: una figura compacta.
        display.show(Image("00000:"
                           "09990:"
                           "99999:"
                           "99999:"
                           "09990"))
    elif resultado == 1:
        # Papel: una hoja rectangular.
        display.show(Image("99999:"
                           "90009:"
                           "90009:"
                           "90009:"
                           "99999"))
    else:
        # Tijera: dos puntas y una unión en el centro.
        display.show(Image("90009:"
                           "09090:"
                           "00900:"
                           "09090:"
                           "90009"))

# Mensaje inicial.
display.scroll("Agita")

# El programa espera continuamente el gesto de agitar.
while True:
    if accelerometer.was_gesture("shake"):
        jugar()
        sleep(1000)
