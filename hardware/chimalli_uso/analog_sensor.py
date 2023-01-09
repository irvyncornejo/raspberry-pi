from gpiozero import MCP3008
import time

lm35 = MCP3008(channel=0)#0 - 1

while True:
    print(lm35.value)
    time.sleep(0.3)