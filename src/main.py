from drive import Drive
from hrc_test import Sensor
from teleop import Teleop
import time

if __name__ == "__main__":
    temp=""
    Controller=Teleop()
    # Change pin numbers before running
    #drive = Drive([1, 2, 3], 4, 5, 6)
    print("Pins are set up correctly...")
    sensor = Sensor(7,11,13,15)
    sensor.st()


