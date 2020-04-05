#!/user/bin/python
import spidev
import time
import os
from gpiozero import Servo

#Abrimos el bus SPI
spi = spidev.SpiDev()#declaramos el objeto 
spi.open(0,0)#SPIO
spi.max_speed_hz= 1000000#declaramos la velocidad de trasnmision 1Mhz

servo = Servo(25)

#Funcion para leer los datos por el protocolo SPI del chip MCP3008
#El integrado tiene 8 canales para el ingreso de la señal. Pero para fines del programa
# el valor del canal de ser un entero 0-7

def leerCanal(canal):#recuerda que hablamos del canal del integrado
    adc = spi.xfer2([1, (8+canal)<<4,0]) 
    data = ((adc[1]&3) << 8) + adc[2]
    return data

def conversionVolts(data, digitos):
    volts = (data * 3.3) / float(1023)#calculo de las muestras
    volts = round(volts,digitos)#aplicamos el método para redondear
    return volts

def posicionX(ejex_posicion):
    posicion = ''
    if(ejex_posicion > 510):
        posicion = 'arriba'
        servo.min()
        return posicion
    
    elif(ejex_posicion < 430):
        posicion = 'abajo'
        servo.max()
        return posicion
    else:
        posicion = 'centro'
        servo.mid()
        return posicion 

#Definimos el valor del canal de los sensores
ejex_canal = 1
ejey_canal = 2

#Definimos el tiempo de retardo entre lectura de los datos
delay = 1



while True:
    
    #leemos el valor del ejex
    ejex_posicion = leerCanal(ejex_canal)
    ejex_volts = conversionVolts(ejex_posicion,2)
    ejex_pos =  posicionX(ejex_posicion)
    
    #leemos el valor del ejey
    ejey_posicion = leerCanal(ejey_canal)
    ejey_volts = conversionVolts(ejey_posicion,2)
    
    #imprimimos los resultados
    print('____________________________________________')
    print('Eje x: {} ({}V) ¿Para dónde se mueve el joystick? {}'.format( ejex_posicion, ejex_volts, ejex_pos  ))
    print('Eje y: {} ({}V)'.format( ejey_posicion, ejey_volts ))
    
    #tiempo de espera para poder repetir el loop
    time.sleep(delay)
    