from gpiozero import RGBLED
from time import sleep
import spidev
import time
import os
global led

led = RGBLED(red=21, green=20, blue=19)

#Abrimos el bus SPI
spi = spidev.SpiDev()#declaramos el objeto 
spi.open(0,0)#SPIO
spi.max_speed_hz= 1000000#declaramos la velocidad de trasnmision 1Mhz

#Funcion para leer los datos por el protocolo SPI del chip MCP3008
#El integrado tiene 8 canales para el ingreso de la señal. Pero para fines del programa
# el valor del canal de ser un entero 0-7

#Definimos el valor del canal de los sensores
flex1 = 0


#Definimos el tiempo de retardo entre lectura de los datos
delay = 0.25

def leerCanal(canal):#recuerda que hablamos del canal del integrado
    adc = spi.xfer2([1, (8+canal)<<4,0]) 
    data = ((adc[1]&3) << 8) + adc[2]
    return data



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

def controlColor(valorPote):
    valor_intensidad = valorPote / 1023
    print(valor_intensidad)
    led.color = (valor_intensidad, valor_intensidad, valor_intensidad)
    sleep(0.2)

while True:
    #leemos el valor del ejex
    flex_uno = leerCanal(flex1)
    #imprimimos los resultados
    print('____________________________________________')
    print('Flex Uno: {}'.format( flex_uno))
    #tiempo de espera para poder repetir el loop
    time.sleep(delay)

    controlColor(flex_uno)

    #led.color = (1, 1, 1)

"""led.color = (0, 0, 0)  # off (1, 1, 1)
sleep(1)
led.color = (1, 0, 1)  # magenta (0, 1, 0)
sleep(1)
led.color = (1, 1, 0)  # yellow (0, 0, 1)
sleep(1)
led.color = (0, 1, 1)  # cyan (1, 0, 0)
sleep(1)


"""

