from tkinter import *
import tkinter.font as tkFont

import spidev
import time
import os




###############################################################################
# Parameters and global variables

# Declare global variables
root = None
dfont = None
frame = None
temp_c = None
lux = None

# Global variable to remember if we are fullscreen or windowed
fullscreen = False

###############################################################################
# Functions

# Toggle fullscreen
def toggle_fullscreen(event=None):

    global root
    global fullscreen

    # Toggle between fullscreen and windowed modes
    fullscreen = not fullscreen
    root.attributes('-fullscreen', fullscreen)
    resize()

# Return to windowed mode
def end_fullscreen(event=None):

    global root
    global fullscreen

    # Turn off fullscreen mode
    fullscreen = False
    root.attributes('-fullscreen', False)
    resize()

# Automatically resize font size based on window size
def resize(event=None):

    global dfont
    global frame

    # Resize font based on frame height (minimum size of 12)
    # Use negative number for "pixels" instead of "points"
    new_size = -max(12, int((frame.winfo_height() / 10)))
    dfont.configure(size=new_size)

# Read values from the sensors at regular intervals
def poll():

    global root
    global temp_c
    global lux

    # Update labels to display temperature and light values
    try:
        val = round(valorLM35, 2)
        temp_c.set(val)
        val = round(valorLM35, 1)
        lux.set(val)
    except:
        pass

    # Schedule the poll() function for another 500 ms from now
    root.after(500, poll)

##############Configuración de los pines
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

###############################################################################
# Main script

# Create the main window
root = Tk()
root.title("Sensor Data")

# Create the main container
frame = Frame(root)

# Lay out the main container (expand to fit window)
frame.pack(fill=BOTH, expand=1)

# Variables for holding temperature and light data
temp_c = DoubleVar()
lux = DoubleVar()

# Create dynamic font for text
dfont = tkFont.Font(size=-24)

# Create widgets
label_temp = Label(frame, text="Temperature:", font=dfont)
label_celsius = Label(frame, textvariable=temp_c, font=dfont)
label_unitc = Label(frame, text="°C", font=dfont)
label_light = Label(frame, text="Light:", font=dfont)
label_lux = Label(frame, textvariable=lux, font=dfont)
label_unitlux = Label(frame, text="lux", font=dfont)
button_quit = Button(frame, text="Quit", font=dfont, command=root.destroy)

# Lay out widgets in a grid in the frame
label_temp.grid(row=0, column=0, padx=5, pady=5, sticky=E)
label_celsius.grid(row=0, column=1, padx=5, pady=5, sticky=E)
label_unitc.grid(row=0, column=2, padx=5, pady=5, sticky=W)
label_light.grid(row=1, column=0, padx=5, pady=5, sticky=E)
label_lux.grid(row=1, column=1, padx=5, pady=5, sticky=E)
label_unitlux.grid(row=1, column=2, padx=5, pady=5, sticky=W)
button_quit.grid(row=2, column=2, padx=5, pady=5)

# Make it so that the grid cells expand out to fill window
for i in range(0, 3):
    frame.rowconfigure(i, weight=1)
for i in range(0, 3):
    frame.columnconfigure(i, weight=1)

# Bind F11 to toggle fullscreen and ESC to end fullscreen
root.bind('<F11>', toggle_fullscreen)
root.bind('<Escape>', end_fullscreen)

# Have the resize() function be called every time the window is resized
root.bind('<Configure>', resize)

# Initialize our sensors
valorLM35 = leerCanal(LM35)

# Schedule the poll() function to be called periodically
root.after(500, poll)

# Start in fullscreen mode and run
toggle_fullscreen()
root.mainloop()
