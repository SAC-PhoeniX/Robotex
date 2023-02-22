# import sacrace
#from pandas import read_csv
from evdev import InputDevice, categorize, ecodes, KeyEvent
#from drive import Drive
import glob
import os
#from drive import Drive
#from sensors import Sensor


class Teleop:
    def ConnectDevice(self,device_name="Logitech Gamepad F710"):
        """This function is ment to connect the device to the desired controller 
        and in order to reconnect to the controller if the connection is lost."""
        
        event_dir = "/dev/input/"
        os.chdir("/dev/input")
        # TEST NEEDED
        self.x=0
        self.y=0
        for file in sorted(glob.glob("event*")):
            print(file)  # TEST
            event_path = file
            tempdevice= InputDevice(event_dir + event_path)
            print(tempdevice.name)
            if tempdevice.name==device_name:#Model Name Here
                break
        else:#if device isn't found
            return
        self.device= InputDevice(event_dir + event_path)
        return 

    def __init__(self,event_path='event3') -> None: #drive: Drive

        self.data = []
        self.events_dir = "/dev/input/"

        # IN case of a change in pins, a change in this line is needed
        #self.Sensor = Sensor(7,11,13,15, sleep_time= 0.1)

        self.ConnectDevice()

    def UpdateInputs(self,timestried=8):

        for i in range(timestried):
            event=self.device.read_one()

            if event==None:
                continue
            
            if event.type == ecodes.EV_ABS:
                absevent = categorize(event)
                if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_RY':
                    y = absevent.event.value
                    #y = (y-127)* -1
                    y /= -2**8
                    y = int(y)
                    self.y=y

                if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_RX':
                    x = absevent.event.value
                    #x = (x - 128) * -1
                    x /= -2**8
                    x = int(x)
                    self.x=x

                # -10 < y < 10
                # if -10 < y and y < 10:
                #     self.y=y
                # if -10 < x and x < 10:
                #     x = 0#y=0 
                #     self.x=x
        
        self.data.append([self.x,self.y])
        return {"angle":self.x,"speed":self.y}



    def UpdateDriver(self, speed: int, angle: int, update_interval: int, timestried=8) -> None:
        for i in range(timestried):
            event=self.device.read_one()

            if event==None:
                continue
            
            if event.type == ecodes.EV_ABS:
                absevent = categorize(event)
                if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_RY':
                    y = absevent.event.value
                    #y = (y-127)* -1
                    y /= -2**8
                    y = int(y)
                    self.y=y

                if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_RX':
                    x = absevent.event.value
                    #x = (x - 128) * -1
                    x /= -2**8
                    x = int(x)
                    self.x=x

                # -10 < y < 10
                if -10 < y and y < 10:
                    self.y=y
                if -10 < x and x < 10:
                    x = 0#y=0 
                    self.x=x
        
        self.data.append([self.x,self.y,self.Sensor.get_distance().values[0],self.Sensor.get_distance().values[1],self.Sensor.get_distance().values[2]])
        self.drive.update(self.x, self.y, update_interval)


if __name__=="__main__":
    a=Teleop()
    while True:
        a.UpdateInputs()
        print(a)
    
    #a.data.to_csv("data1.csv")
