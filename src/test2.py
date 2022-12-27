from evdev import InputDevice, categorize, ecodes, KeyEvent
import os
import glob
def ConnectDevice(device_name="Logitech Gamepad F710"):
        
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
        
        return event_dir + event_path
gamepad = InputDevice(ConnectDevice())
print(gamepad)
x = 0
y = 0
for event in gamepad.read_loop():
    if event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_RY':
            y = absevent.event.value
            #y = (y-127)* -1
            y /= -2**8
            y = int(y)

        if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_RX':
            x = absevent.event.value
            #x = (x - 128) * -1
            x /= -2**8
            x = int(x)

        # -10 < y < 10
        if -10 < y and y < 10:
            y = 0
        if -10 < x and x < 10:
            x = 0#y=0 
        

        print(ecodes.bytype[absevent.event.type][absevent.event.code])
        print(f"x: {x}, y: {y}")
        


    """if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_Z':
        if absevent.event.value > 128 :
            print('right')
            print(absevent.event.value)
        elif absevent.event.value < 127:
            print('left')
            print(absevent.event.value)"""