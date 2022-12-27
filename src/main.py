from drive import Drive
from hrc04 import Sensor

if __name__ == "__main__":
    # Change pin numbers before running
    #drive = Drive([1, 2, 3], 4, 5, 6)
    print("Pins are set up correctly...")
    sensor = Sensor(7,11,13,15)
    print(sensor.distance())


