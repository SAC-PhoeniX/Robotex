# import sacrace
from evdev import InputDevice, ecodes
#from drive import Drive
import glob
import os
from drive import Drive


class Teleop:
    def ConnectDevice(self,device_name="Logitech Gamepad F710"):
        """This function is ment to connect the device to the desired controller 
        and in order to reconnect to the controller if the connection is lost."""
        event_dir = "/dev/input/"
        os.chdir("/dev/input")
        # TEST NEEDED
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
        #self.drive = drive

        self.CENTER_TOLERANCE = 350
        self.STICK_MAX = 65536

        self.axis = {
            ecodes.ABS_X: 'ls_x',  # 0 - 65,536   the middle is 32768
            ecodes.ABS_Y: 'ls_y',
            ecodes.ABS_RX: 'rs_x',
            ecodes.ABS_RY: 'rs_y',
            ecodes.ABS_BRAKE: 'lt',  # 0 - 1023
            ecodes.ABS_GAS: 'rt',

            ecodes.ABS_HAT0X: 'dpad_x',  # -1 - 1
            ecodes.ABS_HAT0Y: 'dpad_y',

            2: "trigger1",
            5: "trigger2"
        }

        self.center = {
            'ls_x': self.STICK_MAX/2,
            'ls_y': self.STICK_MAX/2,
            'rs_x': self.STICK_MAX/2,
            'rs_y': self.STICK_MAX/2
        }

        self.last = {
            'ls_x': self.STICK_MAX/2,
            'ls_y': self.STICK_MAX/2,
            'rs_x': self.STICK_MAX/2,
            'rs_y': self.STICK_MAX/2
        }
            
        self.motorrange = 80
        self.steerrange = 70

        # TEST NEEDED
        self.events_dir = "/dev/input/"

        if event_path == "":
            os.chdir("/dev/input")
            # TEST NEEDED
            for file in sorted(glob.glob("event*")):
                print(file)  # TEST
                event_path = file

        self.ConnectDevice()




    

    def UpdateInputs(self,timestried=10): #TODO the inputs sometimes bug out at 0.5. This can cause the car to crash and get damaged like the bug that was faced last time.

        try:
            for i in range(timestried):
                event=self.device.read_one()

                if event==None:
                    continue

                if event.type == ecodes.EV_ABS:
                    print(event.code)
                    if self.axis[event.code] in ['ls_y', 'rs_x']:
                        self.last[self.axis[event.code]] = event.value
                        value = event.value - self.center[self.axis[event.code]]

                        if abs(value) <= self.CENTER_TOLERANCE:
                            value = 0

                        print("angle:" + str(self.last['rs_x']/self.STICK_MAX))
                        print("speed:" + str(self.last['ls_y']/self.STICK_MAX))
                        ret={"angle":self.last['rs_x']/self.STICK_MAX,"speed":self.last['ls_y']/self.STICK_MAX}#The speed for the controller does not change and stays the same. The controller probably needs to be changed because this is not caused by a software error. 
                        self.last_inputs=ret
                        return ret
            return {"angle":0,"speed":0} #The speed and the angle needs to be returned zero so the car kn ows when to stop
        except:
            self.ConnectDevice()



    def UpdateDriver(self, speed: int, angle: int, update_interval: int) -> None:
        self.drive.update(speed, angle, update_interval)


if __name__=="__main__":
    a=Teleop()
    while True:
        a.UpdateInputs()