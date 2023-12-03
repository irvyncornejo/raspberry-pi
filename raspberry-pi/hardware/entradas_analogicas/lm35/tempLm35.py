#!/user/bin/python
import spidev
import time
import os

#Abrimos el bus SPI
spi = spidev.SpiDev()#declaramos el objeto 
spi.open(0,0)#SPIO
spi.max_speed_hz= 1000000#declaramos la velocidad de trasnmision 1Mhz

#Funcion para leer los datos por el protocolo SPI del chip MCP3008
#El integrado tiene 8 canales para el ingreso de la señal. Pero para fines del programa
# el valor del canal de ser un entero 0-7

def leerCanal(canal):#recuerda que hablamos del canal del integrado
    adc = spi.xfer2([1, (8+canal)<<4,0]) 
    data = ((adc[1]&3) << 8) + adc[2]
    return data

#Definimos el valor del canal de los sensores
LM35 = 0

#Definimos el tiempo de retardo entre lectura de los datos
delay = 0.25

if __name__ == '__main__':
    while True:
        #leemos el valor del sensor LM35
        valorLM35 = leerCanal(LM35)
        
        #Multiplicamos los bits * 330 y dividimos entre 1023 que son las muestras
        #322 en básicamente por el voltaje de referencia y el incremento en grados
        centigrado = ((valorLM35 * 330)  / (1023))
        
        #redondeamos a 3 decimales el valor que obtenemos
        centigrado = round(centigrado, 3)
        
        #imprimimos los resultados
        print('____________________________________________')
        print('La temperatura aproximada es: {} C'.format(centigrado))
        
        #tiempo de espera para poder repetir el loop
        time.sleep(delay)
