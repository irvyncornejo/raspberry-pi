from gpiozero import Servo
from time import sleep

servo1 = Servo(12)
servo2 = Servo(13)

while True:
    servo1.min()
    servo2.min()
    sleep(2)
    servo1.mid()
    servo2.mid()
    sleep(2)
    servo1.max()
    servo2.max()
    sleep(2)
