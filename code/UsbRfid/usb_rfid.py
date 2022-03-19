import os
import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
usb_off = True

try:
    while True:
        id, text = reader.read()
        print(id)
        if id == 246186990289:
            if usb_off:
                usb_off = False
                os.system("sudo ../hub-ctrl -h 1 -P 2 -p 1")
                print("USB Enable")
                time.sleep(5)
                os.system("lsusb")
            elif not usb_off:
                usb_off = True
                os.system("sudo ../hub-ctrl -h 1 -P 2 -p 0")
                print("USB Disable")
                time.sleep(5)
                os.system("lsusb")
        print("-----------------------")
finally:
    GPIO.cleanup()