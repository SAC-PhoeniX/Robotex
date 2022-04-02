from cv2 import HoughLines, imread, cvtColor, IMREAD_GRAYSCALE, Canny
from numpy import pi


class NoImageException(Exception):
    def __str__(self) -> str:
        return "Image with the given path could not be found."


class Road_Detection():
    def __init__(self) -> None:
        # Defines thresholds for Canny detection
        self.HIGHTRESH_CANNY = 50
        self.LOWTHRESH_CANNY = 200

        self.image = None
        self.contourlines = None

    def detect_road(self, image_path):
        self.image = imread(image_path, IMREAD_GRAYSCALE)
        if self.image is None:
            raise NoImageException

        # Detection using Canny
        dst = Canny(self.image, self.LOWTHRESH_CANNY,
                    self.HIGHTRESH_CANNY, False, 3)

        # Hough Lines Transformation
        HoughLines(dst, 1, pi, 200, None, 0, 0)
