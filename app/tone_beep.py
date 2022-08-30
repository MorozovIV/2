from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

t = TonalBuzzer(17)

v1 = ["G4", "C4", "G4", "Ab4", "D4", "Ab4", "G4"]
# v2 = ["B4", "B4", "A4", "A4", "G4"]
# v3 = ["D4", "G4", "G4", "G4", "D4", "E4", "E4", "D4"]

song = [v1]
# song = [v1,v2,v3,v2]

for verse in song:
    for note in verse:
        t.play(note)
        sleep(0.1)
        t.stop()
        sleep(0.02)
    sleep(0.2)