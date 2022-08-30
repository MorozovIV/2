from datetime import datetime
import threading
import time
#from gpiozero import Buzzer
from gpiozero import LED, TonalBuzzer
from gpiozero.tones import Tone

bz = TonalBuzzer(17)
led = LED(5)
cooler = LED(6)
pomp = LED(13)
const_time_led = 6
min_time_cooler = 11
max_time_cooler = 16

def beep():
    v1 = ["G4", "C4", "G4", "Ab4", "D4", "Ab4", "G4"]
    # v2 = ["B4", "B4", "A4", "A4", "G4"]
    # v3 = ["D4", "G4", "G4", "G4", "D4", "E4", "E4", "D4"]

    song = [v1]
    # song = [v1,v2,v3,v2]

    for verse in song:
        for note in verse:
            bz.play(note)
            time.sleep(0.1)
            bz.stop()
            time.sleep(0.02)
        time.sleep(0.2)

beep()


def infiniteloop1():
    while True:
        print('Первый поток')
        now_led = datetime.now()
        current_time_led = now_led.strftime("%H")
        if int(current_time_led) > const_time_led or int(current_time_led) == const_time_led:
            print('LED ON' + current_time_led)
            led.off()
        else:
            print('LED OFF' + current_time_led)
            led.on()
        time.sleep(5)

def infiniteloop2():
    while True:
        print("второй поток")
        now_cooler = datetime.now()
        current_time_cooler = now_cooler.strftime("%H")
        if int(current_time_cooler) > min_time_cooler and int(current_time_cooler) < max_time_cooler:
            print("cooler ON" + current_time_cooler)
            cooler.off()
        else:
            print("cooler OFF" + current_time_cooler)
            cooler.on()
        time.sleep(10)

thread1 = threading.Thread(target=infiniteloop1)
thread1.start()

thread2 = threading.Thread(target=infiniteloop2)
thread2.start()

