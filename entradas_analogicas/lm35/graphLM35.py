import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
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

valorLM35 = leerCanal(LM35)
        
#Multiplicamos los bits * 330 y dividimos entre 1023 que son las muestras
#322 en básicamente por el voltaje de referencia y el incremento en grados
centigrado = ((valorLM35 * 330)  / (1023))


# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

# Initialize communication with TMP102


# This function is called periodically from FuncAnimation
def animate(i, xs, ys):

    # Read temperature (Celsius) from TMP102
    temp_c = round(centigrado, 3)

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(temp_c)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('TMP102 Temperature over Time')
    plt.ylabel('Temperature (deg C)')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()
