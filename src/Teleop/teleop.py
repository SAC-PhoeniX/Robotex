from drive import Drive


class Teleop:
    def __init__(self, drive: Drive) -> None:
        self.drive = drive

    def update(self, speed: int, angle: int, update_interval: int) -> None:
        self.drive.update(speed, angle, update_interval)
