from datetime import datetime
import threading
import time
from gpiozero import LED

led = LED(5)
const_time = 6

def infiniteloop1():
    while True:
        print('Первый поток')
        now = datetime.now()
        current_time = now.strftime("%H")
        if int(current_time) > const_time or int(current_time) == const_time:
            print('LED ON' + current_time)
            led.off()
        else:
            print(now.strftime("%H:%M:%S"))
            led.on()
        time.sleep(1)

def infiniteloop2():
    while True:
        print('Второй поток')
        time.sleep(1)

thread1 = threading.Thread(target=infiniteloop1)
thread1.start()

thread2 = threading.Thread(target=infiniteloop2)
thread2.start()
