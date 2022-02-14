from gpiozero import Motor
from time import sleep

motorA = Motor(forward=23, backward=24)
motorB = Motor(forward=27, backward=22)
while True:
    motorA.forward()
    motorB.forward()
    sleep(5)
    motorA.stop()
    motorB.stop()
    sleep(1)
    motorA.backward()
    motorB.backward()
    sleep(5)
    motorA.stop()
    motorB.stop()
    sleep(1)
