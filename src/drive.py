import RPi.GPIO as gpio
import time


class Drive:
    def __init__(self, pins: list, stop_pin: int, drive_pin: int, steer_pin: int) -> None:
        """Main Drive class. This class is used to control the car's drive system.\n
        pins: list of pins used for the sensors.\n
        stop_pin: pin used for the stop button.\n
        drive_pin: pin used for the drive motor.\n
        steer_pin: pin used for the steering motor.\n
        """

        self.gpio = gpio
        self.sensor_pins = pins
        self.stop_pin = stop_pin
        self.drive_pin = drive_pin
        self.steer_pin = steer_pin

        self.gpio.setmode(self.gpio.Board)

        for pin in self.sensor_pins:
            self.gpio.setup(pin, self.gpio.IN)
        self.gpio.setup(self.stop_pin, self.gpio.IN)

        self.gpio.setup(self.drive_pin, self.gpio.OUT)
        self.gpio.setup(self.steer_pin, self.gpio.OUT)

    def drive(self, speed: int) -> None:
        """Drive the car.\n
        speed: speed of the car. Range from 0 to 100.\n
        """
        self.gpio.PWM(self.drive_pin, speed*(speed <=
                      100 and speed >= 0) + 0*(speed > 100 and speed < 0))

    def steer(self, angle: int) -> None:
        """Steer the car.\n
        angle: angle of the steering wheel. Range from 0 to 100.\n
        """
        self.gpio.PWM(self.steer_pin, angle*(angle <=
                      100 and angle >= 0) + 0*(angle > 100 and angle < 0))

    def update(self, speed: int, angle: int) -> None:
        """Update the drive system.\n
        CREATE ANOTHER LOG FILE FOR THE SENSOR SYSTEM.\n
        """
        with open("LOG.log", "a") as log:
            log.write(f"{time.time()} | {speed} | {angle}")

        self.drive(speed)
        self.steer(angle)
