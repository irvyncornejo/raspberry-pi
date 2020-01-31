from gpiozero import DistanceSensor, LED
from time import sleep

#La máxima distancia que puedemos detectar en nuestra raspberry es de 1m
sensorUltrasonico = DistanceSensor(echo=23, trigger=24)#ECHO -->  23 | TRIGGER --> 24

def conversionCm(sensorUltrasonicoMetros):
    centimetros = (sensorUltrasonicoMetros * 100)#coversión de metros a cm
    centimetrosRedondeo = round(centimetros, 3) #redondeo a 3 decimales
    return centimetrosRedondeo
    
led = LED(25)

while True:
    if __name__ == '__main__':
        print('El objeto está a una distancia de {} m'.format(sensorUltrasonico.distance))        
        sleep(1)
        
        """TODO --> Añadir la función para poder convertir la distancia a cm y redondear a 3 decimales"""
        
        distanciaCm = conversionCm(sensorUltrasonico.distance)
        print('El objeto está a una distancia de {} cm'.format(distanciaCm))
        
        """TODO --> Crear una alarma ya sea con un led o un buzzer, el activador será:
        si el sensor ultrasónico detecta un objeto a menos de 10 cm """
        
        if distanciaCm < 10:
            led.on()
        else:
            led.off()
        
