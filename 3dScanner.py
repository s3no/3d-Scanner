import RPi.GPIO as GPIO
from picamera import PiCamera
import time

imgCount = 1
camera = PiCamera()

def takePhoto():
    global imgCount

    camera.start_preview()
    time.sleep(3)
    camera.capture("tmpImages/image" + str(imgCount) + ".jpg")
    camera.stop_preview()
    imgCount += 1

def spinMotor():
    GPIO.setmode(GPIO.BOARD)
    control_pins = [7,11,13,15]
    for pin in control_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)
    halfstep_seq = [
        [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1]
    ]
    for i in range(64):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq[halfstep] [pin])
            time.sleep(0.001)
    GPIO.cleanup()

#only does 8 photos at one angle. Need to build arm to get more photos at other angles
for x in range(9):
    spinMotor()
    takePhoto()
