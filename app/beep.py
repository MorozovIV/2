from gpiozero import Buzzer
import time

bz = Buzzer(17)

def beep():
    bz.on()
    time.sleep(0.06)
    bz.off()
    time.sleep(0.08)
    bz.on()
    time.sleep(0.06)
    bz.off()

beep()