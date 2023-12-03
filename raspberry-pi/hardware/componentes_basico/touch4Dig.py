from gpiozero import Button
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(2, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(3, GPIO.IN, GPIO.PUD_UP)

"""El obejto Button recibe como parametro el GPIO y
si el boton tiene resistencia de pull-up """
button1 = Button(14, False)
button2 = Button(15, False)
button3 = Button(2)

def wait():
    print('Espera a que el botón se presione para seguir con la  ejecución del programa')

def sumar():
    print(4 + 4)
    
def restar():
    print(4 - 4)

if __name__ == '__main__':
    while True:
        
        if button1.is_pressed:
            print('Boton uno presionado')
        elif button2.is_pressed:
            print('Boton dos presionado')
            
        elif button3.is_pressed:
            print('Boton tres presionado')
        
        


            """          
            #Método esperar a que sea precionado precionado
            button1.wait_for_press()
            wait()
            #
            sleep(3)
            
            if button2.is_pressed:
                print('El botón dos fue presionado')
            else:
                print('No han presionado ningún botón')

            button3.when_pressed = sumar
        button4.when_pressed = restar
        """

