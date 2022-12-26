
# import sacrace
from evdev import InputDevice, ecodes
#from drive import Drive
import glob
import os

"""
By Nick as answer on StackOverflow
https://stackoverflow.com/questions/44934309/how-to-access-the-joysticks-of-a-gamepad-using-python-evdev
"""

CENTER_TOLERANCE = 350
STICK_MAX = 65536

axis = {
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

center = {
    'ls_x': STICK_MAX/2,
    'ls_y': STICK_MAX/2,
    'rs_x': STICK_MAX/2,
    'rs_y': STICK_MAX/2
}

last = {
    'ls_x': STICK_MAX/2,
    'ls_y': STICK_MAX/2,
    'rs_x': STICK_MAX/2,
    'rs_y': STICK_MAX/2
}


def teleop(event_path="",readamt=10):

    
    motorrange = 80
    steerrange = 70

    # TEST NEEDED
    event_dir = "/dev/input/"

    if event_path == "":
        os.chdir("/dev/input")
        # TEST NEEDED
        for file in sorted(glob.glob("event*")):
            print(file)  # TEST
            event_path = file
            tempdevice= InputDevice(event_dir + event_path)
            print(tempdevice.name)
            if tempdevice.name=="Logitech Gamepad F710":#Model Name Here
                break

    device = InputDevice(event_dir + event_path)
    print(device)
    
    print(device.read_one())
    for event in device.read_loop():
        if event.type == ecodes.EV_ABS:
            #print(event.code)
            if axis[event.code] in ['ls_y', 'rs_x']:
                last[axis[event.code]] = event.value

                value = event.value - center[axis[event.code]]

                if abs(value) <= CENTER_TOLERANCE:
                    value = 0

               # drive.drive(-last['rs_x']/STICK_MAX, -
               #             last['ls_y']/STICK_MAX)
                print("angle:" + str(last['rs_x']/STICK_MAX))
                print("speed:" + str(last['ls_y']/STICK_MAX))


if __name__ == "__main__":
    teleop("") #The Gamepad Event on the Rasbperry pi