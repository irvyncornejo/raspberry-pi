from gpiozero import PWMLED
from time import sleep

led = PWMLED(25)

def intensidad(valor):
    intensidad = valor / 100
    led.value = (intensidad)


while True:
    
    if __name__ == '__main__':
        valorIntensidad = float(input('Ingresa la intensidad deseada de 0 a 100: '))
        intensidad(valorIntensidad)
"""        
        led.value = (0)
        sleep(2)
        led.value = (0.25)
        sleep(2)
        led.value = (1)
        sleep(2)
"""
"""TODO --> Realiza un programa que te permita controlar la intensidad del LED, desde la consola.
Recuerda que los valores permitidos son de 0 a 1, esto podrías representarse en procentaje de 0% a 100% """

"""
Las instrucciones para el control de la intensidad luminosa del LED por PWM, están definidas estrictamente para
LEDS con ánodo común. Si se requiere utlizar LEDS con la configuración de cátodo común,
es necesario realizar una operación para invertir el valor del ciclo de trabajo
        
        led.value = (1 - 0)
        sleep(2)
        led.value = (1 - 0.25)
        sleep(2)
        led.value = (1 - 1 )
        sleep(2)
"""