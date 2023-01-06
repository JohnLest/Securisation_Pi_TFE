import json
import os
import time
import requests
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522(bus=1, device=2)
usb_off = True
uri = "http://192.168.0.100:8000"

GPIO.setup(7, GPIO.OUT)
GPIO.output(7, False)
try:
    while True:
        id, text = reader.read()
        print(id)
        req = requests.post(f"{uri}/user/rfid", data=json.dumps({"rfid": f"{id}"}), timeout=10 )
        json = req.json()
        print(f"{req.status_code},  {json}")
        if json  == "OK":
            if usb_off:
                usb_off = False
                # os.system("sudo ../hub-ctrl -h 1 -P 2 -p 1")
                print("USB Enable")
                GPIO.output(7, True)
                time.sleep(5)
                # os.system("lsusb")
            elif not usb_off:
                usb_off = True
                # os.system("sudo ../hub-ctrl -h 1 -P 2 -p 0")
                print("USB Disable")
                GPIO.output(7, False)
                time.sleep(5)
                # os.system("lsusb")
        print("-----------------------")
finally:
    GPIO.cleanup()

