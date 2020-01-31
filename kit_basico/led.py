from gpiozero import LED
from time import sleep

led0 = LED(25)#Dentro de los parentesis declaramos el GPIO al que está conectado el led

"""
led1 = LED(17)
led2 = LED(27)
led3 = LED(22)
led4 = LED(10)
"""

def estadoLeds(estado):
    if estado == 'encender':
        led0.on()
    elif estado == 'apagar':
        led0.off()
    else:
        led0.off()
    

while True:
    print('Bienvenido recuerde que puede apagar o encender los leds ')
    
    if __name__ == '__main__':
        
        estado = input('ingrese el estado de los leds: ')
        estadoLeds(estado)
        """led0.on()
        sleep(1.5)
        led0.off()
        sleep(1.5)"""
        
        """TODO --> conectar 4 led restantes y controla el encendido y agrado de los mismos"""
        """TODO --> Controlar el encendido y apagado de los led mediente la consola:
           si el usuario ingresa encender todo los leds se encienden y si el usuario ingresa apagar
           realiza la accion de apagar todos los leds""" 
        
    