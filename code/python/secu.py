import RPi.GPIO as io
import time

io.setmode(io.BCM)
io.setup(22, io.OUT)
io.setup(23, io.IN)

while True:
    io.output(22, True)
    if io.input(23) == 1:
        print("OK")
    else:
        print("Nop")
        
    io.output(22, False)
    time.sleep(5)
io.cleanup()