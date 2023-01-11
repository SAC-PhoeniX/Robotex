import RPi.GPIO as gpio
import time


class Drive:
    def __init__(self, stop_pin: int, drive_pin: int, steer_pin: int) -> None:
        """Main Drive class. This class is used to control the car's drive system.\n
        stop_pin: pin used for the stop button.\n
        drive_pin: pin used for the drive motor.\n
        steer_pin: pin used for the steering motor.\n
        """

        self.MAX_STEER_RANGE = 100
        self.MAX_DRIVE_RANGE = 100
        self.MIN_STEER_RANGE = 0
        self.MIN_DRIVE_RANGE = 0

        self.gpio = gpio
        self.stop_pin, self.drive_pin, self.steer_pin = stop_pin, drive_pin, steer_pin

        # Setting the board mode up
        self.gpio.setmode(self.gpio.BOARD)

        # Setting the pins up
        self.gpio.setup(self.stop_pin, self.gpio.IN)
        self.gpio.setup(self.drive_pin, self.gpio.OUT)
        self.gpio.setup(self.steer_pin, self.gpio.OUT)

    def drive(self, speed: int) -> None:
        """Drive the car.\n
        speed: speed of the car. Range from 0 to 100.\n
        """
        self.gpio.PWM(self.drive_pin, speed*(speed <= self.MAX_DRIVE_RANGE and speed >= self.MIN_DRIVE_RANGE) + 0*(speed > self.MAX_DRIVE_RANGE and speed < self.MIN_DRIVE_RANGE))

    def steer(self, angle: int) -> None:
        """Steer the car.\n
        angle: angle of the steering wheel. Range from 0 to 100.\n
        """
        self.gpio.PWM(self.steer_pin, angle*(angle <= self.MAX_STEER_RANGE and angle >= self.MIN_STEER_RANGE) + 0*(angle > self.MAX_STEER_RANGE and angle < self.MIN_STEER_RANGE))

    def update(self, speed: int, angle: int) -> None:
        """Update the drive system.\n
        CREATE ANOTHER LOG FILE FOR THE SENSOR SYSTEM.\n
        """
        with open("/logs/LOG.log", "a") as log:
            log.write(f"{time.time()} | {speed} | {angle}")

        self.drive(speed)
        self.steer(angle)
