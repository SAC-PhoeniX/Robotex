from drive import Drive
from hrc04 import Sensor
from teleop import Teleop

if __name__ == "__main__":
    temp=""
    Controller=Teleop()
    # Change pin numbers before running
    #drive = Drive([1, 2, 3], 4, 5, 6)
    print("Pins are set up correctly...")
    sensor = Sensor(7,11,13,15)
    while True:
        print(sensor.distance(max_delay=0.2))#TODO: The sensors can be made asnyronous to not block the main loop or the architecture of the main loop can be changed.
        print(Controller.UpdateInputs()) #TODO: the inputs sometimes say that there is input but there isn't. This bug needs to be fixed.
    


