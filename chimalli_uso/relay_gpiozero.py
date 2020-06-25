from gpiozero import LED as Rele
from gpiozero import Button

import time

_RELAY_1 = Rele(4)
boton_1 = Button(14, False)

if __name__ == '__main__':
    while True:
        if boton_1.is_pressed:
            _RELAY_1.off()#Prender
            time.sleep(1)
        else:
            _RELAY_1.on()#Apagar
            time.sleep(1)
            