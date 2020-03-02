from gpiozero import RGBLED
from time import sleep
global led
led = RGBLED(red=2, green=4, blue=3)

def coloresBase():
    
    #Todo apagados
    led.color = (1, 1, 1)
    sleep(1)
    #Rojo maxima intensidad
    led.color = (0, 1, 1)
    sleep(1)
    #verde  maxima intensidad
    led.color = (1, 0, 1)
    sleep(1)
    #Azul  maxima intensidad
    led.color = (1, 1, 0)
    sleep(1)
    #Todos a media intensidad
    led.color = (0.5, 0.5, 0.5)
    sleep(1)
    #"Blanco" Todos máxima intensidad
    led.color = (0, 0, 0)
    sleep(1)

coloresBase()

"""led.color = (0, 0, 0)  # off (1, 1, 1)
sleep(1)
led.color = (1, 0, 1)  # magenta (0, 1, 0)
sleep(1)
led.color = (1, 1, 0)  # yellow (0, 0, 1)
sleep(1)
led.color = (0, 1, 1)  # cyan (1, 0, 0)
sleep(1)


"""

