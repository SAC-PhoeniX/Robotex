from RPi.GPIO import setmode, BOARD, setup, output, input, cleanup, IN, OUT
from time import time, sleep
""""This script is for the initialization of the Distance Sensors"""
class Sensor:
    def __init__(self, trig_pin, echo1, echo2, echo3):
        """Enter the trigger pin, first sensor, second sensor and third sensor."""
        self.trigPIN = trig_pin
        self.echo1 = echo1
        self.echo2 = echo2
        self.echo3 = echo3
        self.inputs=[echo1,echo2,echo3]
        setmode(BOARD)
        setup(self.trigPIN, OUT)
        setup(self.echo1, IN)
        setup(self.echo2, IN)
        setup(self.echo3, IN)

    def distance(self,tometers=True,max_delay=0.25):
        """Returns the measurement done by the Distance sensors. tometers(bool) argument automaticaly converts the time it takes the signal to come back to meters. If this parameter is false, the sensor will return the amount of time it takes for the signal to come back.
        max_delay decides how long the script should wait at maximum. If the time is exceeded, the script returns a none to that sensor's measurement."""
        output(self.trigPIN, True)
        sleep(0.00001)
        output(self.trigPIN, False)

        test1S = time()
        sleep(0.0001)
        retlist=[None for i in range(3)]
        while test1S+max_delay>time():
            for i in range(3):
                if  retlist[i]!=None:
                    continue
                if input(self.inputs[i])==0:
                    retlist[i]=time()-test1S
        if tometers:

            return [17150*i if i != None else None for i in retlist ]#converts to meter
        return retlist
        







        """        
            while input(self.echo1) == 0:
            print(1)
            pulse1_start = time()
        
        while input(self.echo1) == 1:
            print(2)
            pulse1_end = time()

        while input(self.echo2) == 0:
            print(3)
            pulse2_start = time()

        while input(self.echo2) == 1:
            print(4)
            pulse2_end = time()
        
        while input(self.echo3) == 0:
            print(5)
            pulse3_start = time()

        while input(self.echo3) == 1:
            print(6)
            pulse3_end = time()"""


        #return [pu]

if __name__=="__main__":
    Sensors=Sensor(7,11,13,15)#7 trigger, 11,13,15 are from right to left (if faced towards the viewpoint of the sensors(11 has green output cable))
    while True:

        print(Sensors.distance()[0])

"""echoPIN = 11
triggerPIN = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(echoPIN,GPIO.IN)
GPIO.setup(triggerPIN,GPIO.OUT)

print("kjvdfng")
def distance ():
    GPIO.output(triggerPIN,True)
    time.sleep(0.00001)
    GPIO.output(triggerPIN,False)

    while GPIO.input(echoPIN) == 0:
        pulse_start = time.time()

    while GPIO.input(echoPIN) == 1:
        end_time = time.time()

    duration = end_time - pulse_start
    dist = duration * 17150
    return dist

try:
    while True:
        print(distance())
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Measurement stopped")
    GPIO.cleanup()"""
    

