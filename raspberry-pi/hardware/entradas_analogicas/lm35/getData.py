#!/user/bin/python
import spidev
from time import sleep
import os 
import matplotlib.pyplot as plt

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

def convertirCentigrados(valorLM35):
    centigrado = ((valorLM35 * 330)  / (1023))
    centigrado = round(centigrado, 3)
    return centigrado

def escribirDatos(centigrados):
    dataSet.append(centigrados)
    #print(dataSet)
    return dataSet

def crearGrafica(temperaturas):
    plt.plot(temperaturas)
    plt.title('LM35')
    plt.ylabel('Temperaturas')
    plt.xlabel('Intervalos')
    plt.show()
#Canal
LM35 = 0
#Definimos el tiempo de retardo entre lectura de los datos
delay = 0.25

if __name__ == '__main__':
    
    dataSet = list() 
    datos = 0
    while datos < 100:
        valorLM35 = leerCanal(LM35)
        centigrados = convertirCentigrados(valorLM35)
        temperaturas = escribirDatos(centigrados)
        sleep(delay)
        datos +=1
        
    #print(temperaturas)
    crearGrafica(temperaturas)