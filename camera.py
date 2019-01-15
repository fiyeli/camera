#!/usr/bin/env  python
from picamera import PiCamera
import time
import os

camera = PiCamera()

# Set the camera resolution in order to have processable images
camera.resolution = (1024, 768)

camera.start_preview()
time.sleep(2) # Warming-up camera
# Capturing image and storing in the right place and with the right name (<timestamp>.jpg)
camera.capture(os.getenv('FIYELI_IMAGES') + "/" + str(int(time.time())) + ".jpg")
camera.stop_preview()