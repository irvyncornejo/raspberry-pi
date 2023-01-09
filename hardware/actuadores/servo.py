from gpiozero import Servo, LED
from time import sleep

servo = Servo(17)
buzzer = LED(2)


while True:
    servo.min()
    buzzer.on()
    sleep(2)
    servo.mid()
    buzzer.off()
    sleep(2)
    servo.max()
    sleep(2)