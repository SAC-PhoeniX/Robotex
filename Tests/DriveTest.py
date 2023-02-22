# Include the library files
import RPi.GPIO as GPIO
from time import sleep
from src.drive import Drive

d = Drive()
# Include the motor control pins
#TODO: Pins overlap with prexistting sensor circuitery but since the sensor circuits dont exist right now it fine. Switch sensor pins or motor pins
#TODO: make the ENA Pins the same pin so that a single pin can be a switch
#The speed control idea is canceled

#pins for motor 1(left),
ENA = 17  
IN1 = 27 #Foward pin for the motor
IN2 = 22

#pins for motor 2(right), currently doesnt work
ENA2=37
IN3=35
IN4=33

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)
GPIO.setup(ENA,GPIO.OUT)
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(ENA2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT) 
GPIO.setup(IN4,GPIO.OUT)


def forward(): #foward is correct
    GPIO.output(ENA,GPIO.HIGH)
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(ENA2,GPIO.HIGH)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)

def backward():
    GPIO.output(ENA,GPIO.HIGH)
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.HIGH)
    GPIO.output(ENA2,GPIO.HIGH)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.HIGH)

def stop():
    GPIO.output(ENA,GPIO.LOW)
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(ENA2,GPIO.LOW)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.LOW)


try:
    while True:
        d.forward()
        sleep(0.2)
        d.backward()
        sleep(0.2)
        d.right()
        sleep(0.2)
        d.left()
        sleep(0.2)
        stop()
        quit()
except:

    stop()
    quit()
