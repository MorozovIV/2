import RPi.GPIO as GPIO
import time
import os
import datetime

GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)


# Получаем температуру
def gettemp():
    if os.path.isdir("id датчика"):  # Если датчик подключён, то считываем значение
        tfile2 = open("/sys/bus/w1/devices/id датчика")
        ttext2 = tfile2.read()
        tfile2.close()
        temp2 = ttext2.split("\n")[1].split(" ")[9]
        t2 = float(temp2[2:]) / 1000
        print
        t2
    else:  # если нет, то задаём дефолтное
        print('File not found')
        t2 == 24
    return t2


t2 = 24  # Задаём дефолтное значение для датчика
while True: вечный
цикл
t2 = gettemp()
if t2 < 24:  # Если температура меньше 24, то закрываем окно в течение секунды

    GPIO.output(37, 1)
    print("close1")
    time.sleep(1)
    GPIO.output(37, 0)

elif t2 > 26:  # Если больше 26, то открываем окно в течение секунды
    GPIO.output(35, 1)
    print("open1")
    time.sleep(2)
    GPIO.output(35, 0)

else:  # Иначе ничего не делаем
    print("none1")
time.sleep(180)  # Ждём 3 минуты

# Опять читаем температуру
t2 = gettemp()

# Всё то же самое, только со вторым окном.
if t2 < 24:
    GPIO.output(33, 1)
    print("close2")
    time.sleep(1)
    GPIO.output(33, 0)

elif t2 > 26:

    GPIO.output(31, 1)
    print("open2")
    time.sleep(1)
    GPIO.output(31, 0)


else:
    print("none2")

# Опять ждём 3 минуты
time.sleep(180)