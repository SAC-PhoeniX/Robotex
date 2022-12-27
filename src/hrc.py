from RPi.GPIO import setmode, BOARD, setup, output, input, cleanup, IN, OUT
from time import time, sleep
from threading import Thread

class Sensor:
    def __init__(self, trig_pin, echo1, echo2, echo3, sleep_time) -> None:
        self.trigPIN = trig_pin
        self.echo1 = echo1
        self.echo2 = echo2
        self.echo3 = echo3

        self.echo1variable = None
        self.echo2variable = None
        self.echo3variable  = None
        self.sleep_time = sleep_time

    
        setmode(BOARD)
        setup(self.trigPIN, OUT)
        setup(self.echo1, IN)
        setup(self.echo2, IN)
        setup(self.echo3, IN)
        sleep(0.1)
        self.start()

    def distance1(self, echopin, empty):
        
        while True:
            try:
                output(self.trigPIN, True)
                sleep(0.00001)
                output(self.trigPIN, False)

                while input(echopin) == 0:
                    pulse1_start = time()
                
                while input(echopin) == 1:
                    pulse1_end = time()
                
                self.echo1variable = (pulse1_end- pulse1_start) * 17150
                sleep(self.sleep_time)
            except:
                continue

    def distance2(self, echopin, empty):
        
        while True:
            try:

                output(self.trigPIN, True)
                sleep(0.00001)
                output(self.trigPIN, False)

                while input(echopin) == 0:
                    pulse1_start = time()
                
                while input(echopin) == 1:
                    pulse1_end = time()
                
                self.echo2variable = (pulse1_end- pulse1_start) * 17150
                sleep(self.sleep_time)
            except:
                continue

    def distance3(self, echopin, empty):
        while True:
            try:
                output(self.trigPIN, True)
                sleep(0.00001)
                output(self.trigPIN, False)

                while input(echopin) == 0:
                    pulse_start = time()
                
                while input(echopin) == 1:
                    pulse_end = time()
                
                self.echo3variable = (pulse_end- pulse_start) * 17150
                sleep(self.sleep_time)
            except:
                continue

    def start(self):
        self.x = Thread(target=self.distance1, args=(self.echo1, self.echo1variable))
        self.y = Thread(target=self.distance2, args=(self.echo2, self.echo2variable))
        self.z = Thread(target=self.distance3, args=(self.echo3, self.echo3variable))
        self.x.start()
        self.y.start()
        self.z.start()





    def distance(self):
        return {"sensor_1": self.echo1variable, "sensor_2": self.echo2variable, "sensor_3": self.echo3variable}


x = Sensor(7,11,13,15, sleep_time= 0.1)
for i in range(10):
    print(x.distance())
    sleep(0.1)#sleep olmazsa None döndürüyor

cleanup()

