import RPi.GPIO as gpio
import time


class Drive:
    def __init__(self) -> None:
        """Main Drive class. This class is used to control the car's drive system.\n
        stop_pin: pin used for the stop button.\n
        drive_pin: pin used for the drive motor.\n
        steer_pin: pin used for the steering motor.\n
        """

        self.MAX_STEER_RANGE = 100
        self.MAX_DRIVE_RANGE = 100
        self.MIN_STEER_RANGE = 0
        self.MIN_DRIVE_RANGE = 0

        self.gpio = gpio
        # self.stop_pin, self.drive_pin, self.steer_pin = stop_pin, drive_pin, steer_pin

        # # Setting the board mode up
        # self.gpio.setmode(self.gpio.BOARD)

        # # Setting the pins up
        # self.gpio.setup(self.stop_pin, self.gpio.IN)
        # self.gpio.setup(self.drive_pin, self.gpio.OUT)
        # self.gpio.setup(self.steer_pin, self.gpio.OUT)

        #pins for motor 1(left),
        self.ENA = 17  
        self.IN1 = 27 #Foward pin for the motor
        self.IN2 = 22

        #pins for motor 2(right)
        self.ENA2=37
        self.IN3=35 #Forward pin for the motor
        self.IN4=33

        self.gpio.setmode(self.gpio.BCM)
        self.gpio.setwarnings(True)
        self.gpio.setup(self.ENA,self.gpio.OUT)
        self.gpio.setup(self.IN1,self.gpio.OUT)
        self.gpio.setup(self.IN2,self.gpio.OUT)
        self.gpio.setup(self.ENA2,self.gpio.OUT)
        self.gpio.setup(self.IN3,self.gpio.OUT) 
        self.gpio.setup(self.IN4,self.gpio.OUT)

    def forward(self) -> None:
        """Drive the car.\n
        speed: speed of the car. Range from 0 to 100.\n
        """
        self.GPIO.output(self.ENA,self.GPIO.HIGH)
        self.GPIO.output(self.IN1,self.GPIO.HIGH)
        self.GPIO.output(self.IN2,self.GPIO.LOW)
        self.GPIO.output(self.ENA2,self.GPIO.HIGH)
        self.GPIO.output(self.IN3,self.GPIO.HIGH)
        self.GPIO.output(self.IN4,self.GPIO.LOW)

    def back(self) -> None:
        """Drive the car.\n
        speed: speed of the car. Range from 0 to 100.\n
        """
        self.GPIO.output(self.ENA,self.GPIO.HIGH)
        self.GPIO.output(self.IN1,self.GPIO.LOW)
        self.GPIO.output(self.IN2,self.GPIO.HIGH)
        self.GPIO.output(self.ENA2,self.GPIO.HIGH)
        self.GPIO.output(self.IN3,self.GPIO.LOW)
        self.GPIO.output(self.IN4,self.GPIO.HIGH)

    def right(self):
        self.GPIO.output(self.ENA,self.GPIO.HIGH)
        self.GPIO.output(self.IN1,self.GPIO.LOW)
        self.GPIO.output(self.IN2,self.GPIO.HIGH)
        self.GPIO.output(self.ENA2,self.GPIO.HIGH)
        self.GPIO.output(self.IN3,self.GPIO.HIGH)   
        self.GPIO.output(self.IN4,self.GPIO.LOW)  

    def left(self):
        self.GPIO.output(self.ENA,self.GPIO.HIGH)
        self.GPIO.output(self.IN1,self.GPIO.HIGH)
        self.GPIO.output(self.IN2,self.GPIO.LOW)
        self.GPIO.output(self.ENA2,self.GPIO.HIGH)
        self.GPIO.output(self.IN3,self.GPIO.LOW) 
        self.GPIO.output(self.IN4,self.GPIO.HIGH)     
