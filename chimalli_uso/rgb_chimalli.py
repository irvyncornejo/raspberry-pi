from gpiozero import RGBLED, Buzzer
import time

rgb = RGBLED(red=21, green=20, blue=19)
buzzer = Buzzer(18)

rgb.color = (0, 1, 0)
buzzer.off()
time.sleep(2)
rgb.color = (1, 0, 0)
time.sleep(2)
rgb.color = (1, 1, 0)
time.sleep(2)
rgb.color = (1, 1, 1)

