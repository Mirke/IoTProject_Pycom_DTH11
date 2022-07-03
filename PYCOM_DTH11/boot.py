import pycom
# Data is sent to Pybytes. Needs to flashed with Pybyte firmware
import time
from machine import Pin
from dht import DHT # https://github.com/JurassicPork/DHT_PyCom

#Helper function - How many minutes it should sleep.
def minutes(howMany):
    return 60 * howMany
sleepTime = minutes(30)

#Turns the led on LoPy4 and Expansion3 off.
led = Pin('P9', mode = Pin.OUT)
led.value(1)
pycom.heartbeat(False)

# Pin for the DTH11 funny they call it DHT here.
th = DHT(Pin('P23', mode=Pin.OPEN_DRAIN))
time.sleep(2)

# Main loop for the program.
while True:
    result = th.read()
    while not result.is_valid():
        time.sleep(.5)
        result = th.read()
    print('Temp:', result.temperature)
    print('RH:', result.humidity)
    pybytes.send_signal(1,result.temperature)
    pybytes.send_signal(2,result.humidity)

    time.sleep(sleepTime)
