from machine import Pin #Import Pin from machine as we are using LED pin
from time import sleep #Import Sleep from Time as we need for delay

led = Pin(25, Pin.OUT) #The on board LED on Pico is on Pin 25

while True: 
     led.toogle() #changing state of LED
     sleep(0.5) #delay between Toogle