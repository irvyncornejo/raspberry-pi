from gpiozero import Button
from time import sleep

"""El obejto Button recibe como parametro el GPIO y
si el boton tiene resistencia de pull-up """
button1 = Button(14, False)
button2 = Button(15, False)
button3 = Button(18, False)
button4 = Button(23, False)
def wait():
    print('Espera a que el botón se presione para seguir con la  ejecución del programa')

def sumar():
    print(4 + 4)
    
def restar():
    print(4 - 4)

if __name__ == '__main__':
    while True:
            
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
        
        

