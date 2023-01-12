from drive import Drive
from sensors import Sensor
#from teleop import Teleop
from time import sleep
from threading import Thread

#TODO Stop Button and Function MUST Be Added
#TODO Autonomous Mode Will Be Added

#PINS
"""
Drive Motor: 
Steering Motor:
Sensors - Trig: 7
Sensors - Echo: 11 13 15
"""

class Main:
    def __init__(self) -> None:
        #self.Drive = Drive([1, 2, 3], 4, 5, 6)
        self.sensors = Sensor(7,11,13,15)
        #self.teleop_ = Teleop()

        self.distance = None
        self.running = True

    def stop(self):
        self.running = False
        quit()

    def start(self):
        sensors = Sensor()
        print(sensors.echo1variable)
        #sensors.start()
        
        while self.running:
            print(sensors.distance())
            sleep(0.1)


    def teleop(self):
        pass


if __name__ == "__main__":
    main = Main()
    main.start()
