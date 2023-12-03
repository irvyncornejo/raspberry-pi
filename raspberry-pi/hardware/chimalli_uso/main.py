import RPi.GPIO as GPIO
import time
#nombres en munusculas valores no contantes y palabras compuestas separadas por guion bajo
#Constantes se declaran en mayusculas e inician con un guion bajo

_RELE_1 = 4 

GPIO.setmode(GPIO.BCM)#Configuración 
GPIO.setwarnings(False)#anúlar advertencias 

GPIO.setup(_RELE_1, GPIO.OUT)#GPIO.INPUT

def prender_reles(tiempo):
    for i in range(10):
        GPIO.output(_RELE_1, GPIO.HIGH)#Estado LOW - HIGH
        time.sleep(tiempo)
        GPIO.output(_RELE_1, GPIO.LOW)
        time.sleep(tiempo)
        print('Ciclo {}'.format(i))
        
    return 'Relay dejaron de funcionar'

if __name__ == '__main__':
    while True:
        tiempo = float(input("Escribe el tiempo de sleep: "))
        print(prender_reles(tiempo))

