#imports
# Camera functions to control rasp pi camera
from picamera import PiCamera
from time import sleep
from PIL import Image

#gpiozero API to control gpio
from gpiozero import *

import sys
import pyocr
import pyocr.builders

def convert(character):
    # space character check, turn off all actuators
    if character == 'a':
        piezo1.off()
        piezo2.off()
        piezo3.off()
        piezo4.off()
        piezo5.off()
        piezo6.off()

    # Beginning of Alphabet
    elif character == 'a':
        piezo1.on()
        piezo2.off()
        piezo3.off()
        piezo4.off()
        piezo5.off()
        piezo6.off()
    elif character == 'b':
        piezo1.on()
        piezo2.on()
        piezo3.off()
        piezo4.off()
        piezo5.off()
        piezo6.off()
    elif character == 'c':
        piezo1.on()
        piezo2.off()
        piezo3.off()
        piezo4.on()
        piezo5.off()
        piezo6.off()
    elif character == 'd':
        piezo1.on()
        piezo2.off()
        piezo3.off()
        piezo4.on()
        piezo5.on()
        piezo6.off()
    elif character == 'e':
        piezo1.on()
        piezo2.off()
        piezo3.off()
        piezo4.off()
        piezo5.on()
        piezo6.off()
    elif character == 'f':
        piezo1.on()
        piezo2.on()
        piezo3.off()
        piezo4.on()
        piezo5.off()
        piezo6.off()
    elif character == 'g':
        piezo1.on()
        piezo2.on()
        piezo3.off()
        piezo4.on()
        piezo5.on()
        piezo6.off()
    elif character == 'h':
        piezo1.on()
        piezo2.on()
        piezo3.off()
        piezo4.off()
        piezo5.on()
        piezo6.off()
    elif character == 'i':
        piezo1.off()
        piezo2.on()
        piezo3.off()
        piezo4.on()
        piezo5.off()
        piezo6.off()
    elif character == 'j':
        piezo1.off()
        piezo2.on()
        piezo3.off()
        piezo4.on()
        piezo5.on()
        piezo6.off()
    elif character == 'k':
        piezo1.on()
        piezo2.off()
        piezo3.on()
        piezo4.off()
        piezo5.off()
        piezo6.off()
    elif character == 'l':
        piezo1.on()
        piezo2.on()
        piezo3.on()
        piezo4.off()
        piezo5.off()
        piezo6.off()
    elif character == 'm':
        piezo1.on()
        piezo2.off()
        piezo3.on()
        piezo4.on()
        piezo5.off()
        piezo6.off()
    elif character == 'n':
        piezo1.on()
        piezo2.off()
        piezo3.on()
        piezo4.on()
        piezo5.on()
        piezo6.off()
    elif character == 'o':
        piezo1.on()
        piezo2.off()
        piezo3.on()
        piezo4.off()
        piezo5.on()
        piezo6.off()
    elif character == 'p':
        piezo1.on()
        piezo2.on()
        piezo3.on()
        piezo4.on()
        piezo5.off()
        piezo6.off()
    elif character == 'q':
        piezo1.on()
        piezo2.on()
        piezo3.on()
        piezo4.on()
        piezo5.on()
        piezo6.off()
    elif character == 'r':
        piezo1.on()
        piezo2.on()
        piezo3.on()
        piezo4.off()
        piezo5.on()
        piezo6.off()
    elif character == 's':
        piezo1.off()
        piezo2.on()
        piezo3.on()
        piezo4.on()
        piezo5.off()
        piezo6.off()
    elif character == 't':
        piezo1.off()
        piezo2.on()
        piezo3.on()
        piezo4.on()
        piezo5.on()
        piezo6.off()
    elif character == 'u':
        piezo1.on()
        piezo2.off()
        piezo3.on()
        piezo4.off()
        piezo5.off()
        piezo6.on()
    elif character == 'v':
        piezo1.on()
        piezo2.on()
        piezo3.on()
        piezo4.off()
        piezo5.off()
        piezo6.on()
    elif character == 'w':
        piezo1.off()
        piezo2.on()
        piezo3.off()
        piezo4.on()
        piezo5.on()
        piezo6.on()
    elif character == 'x':
        piezo1.on()
        piezo2.off()
        piezo3.on()
        piezo4.on()
        piezo5.off()
        piezo6.on()
    elif character == 'y':
        piezo1.on()
        piezo2.off()
        piezo3.on()
        piezo4.on()
        piezo5.on()
        piezo6.on()
    elif character == 'z':
        piezo1.on()
        piezo2.off()
        piezo3.on()
        piezo4.off()
        piezo5.on()
        piezo6.on()

    # Numbers start here
    # number indicator is 3456
    elif character in '0123456789':
        
        piezo1.off()
        piezo2.off()
        piezo3.on()
        piezo4.on()
        piezo5.on()
        piezo6.on()
        sleep(2)

        if character == '1':
            piezo1.on()
            piezo2.off()
            piezo3.off()
            piezo4.off()
            piezo5.off()
            piezo6.off()
        elif character == '2':
            piezo1.on()
            piezo2.on()
            piezo3.off()
            piezo4.off()
            piezo5.off()
            piezo6.off()
        elif character == '3':
            piezo1.on()
            piezo2.off()
            piezo3.off()
            piezo4.on()
            piezo5.off()
            piezo6.off()
        elif character == '4':
            piezo1.on()
            piezo2.off()
            piezo3.off()
            piezo4.on()
            piezo5.on()
            piezo6.off()
        elif character == '5':
            piezo1.on()
            piezo2.off()
            piezo3.off()
            piezo4.off()
            piezo5.on()
            piezo6.off()
        elif character == '6':
            piezo1.on()
            piezo2.on()
            piezo3.off()
            piezo4.on()
            piezo5.off()
            piezo6.off()
        elif character == '7':
            piezo1.on()
            piezo2.on()
            piezo3.off()
            piezo4.on()
            piezo5.on()
            piezo6.off()
        elif character == '8':
            piezo1.on()
            piezo2.on()
            piezo3.off()
            piezo4.off()
            piezo5.on()
            piezo6.off()
        elif character == '9':
            piezo1.off()
            piezo2.on()
            piezo3.off()
            piezo4.on()
            piezo5.off()
            piezo6.off()
        elif character == '0':
            piezo1.off()
            piezo2.on()
            piezo3.off()
            piezo4.on()
            piezo5.on()
            piezo6.off()

    # Punctuation starts here
    elif character == ',':
        piezo1.off()
        piezo2.on()
        piezo3.off()
        piezo4.off()
        piezo5.off()
        piezo6.off()
    elif character == ';':
        piezo1.off()
        piezo2.on()
        piezo3.on()
        piezo4.off()
        piezo5.off()
        piezo6.off()
    elif character == ':':
        piezo1.off()
        piezo2.on()
        piezo3.off()
        piezo4.off()
        piezo5.on()
        piezo6.off()
    elif character == '.':
        piezo1.off()
        piezo2.on()
        piezo3.off()
        piezo4.off()
        piezo5.on()
        piezo6.on()
    elif character == '?':
        piezo1.off()
        piezo2.on()
        piezo3.on()
        piezo4.off()
        piezo5.off()
        piezo6.on()
    elif character == '(':
        piezo1.off()
        piezo2.off()
        piezo3.off()
        piezo4.off()
        piezo5.on()
        piezo6.off()

        sleep(1)

        piezo1.on()
        piezo2.on()
        piezo3.off()
        piezo4.off()
        piezo5.off()
        piezo6.on()
   elif character == ')':
        piezo1.off()
        piezo2.off()
        piezo3.off()
        piezo4.off()
        piezo5.on()
        piezo6.off()

        sleep(1)

        piezo1.off()
        piezo2.off()
        piezo3.off()
        piezo4.on()
        piezo5.on()
        piezo6.off()
    elif character == '/':
        piezo1.off()
        piezo2.off()
        piezo3.off()
        piezo4.on()
        piezo5.on()
        piezo6.on()

        sleep(1)

        piezo1.off))
        piezo2.off()
        piezo3.on()
        piezo4.on()
        piezo5.off()
        piezo6.off()
    elif character == '\':
        piezo1.off()
        piezo2.off()
        piezo3.off()
        piezo4.on()
        piezo5.on()
        piezo6.on()

        sleep(1)

        piezo1.on()
        piezo2.off()
        piezo3.off()
        piezo4.off()
        piezo5.off()
        piezo6.on()

# initialize camera module
camera = PiCamera()

# intialize pyocr
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'libtesseract'

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = langs[0]
print("Will use lang '%s'" % (lang))

#camera.start_preview()
#sleep(10)
#camera.capture('/home/pi/Capstone/test.png')       
#camera.stop_preview()


#txt = tool.image_to_string(
#    Image.open('/home/pi/Capstone/test.png'),
#    lang="eng",
#    builder=pyocr.builders.TextBuilder()
#)
#print(txt)
# txt is a Python string

# Piezoeletric actuator layout corresponding to numbered piezo variables
# 1 4
# 2 5
# 3 6
piezo1 = OutputDevice(17)
piezo2 = OutputDevice(18)
piezo3 = OutputDevice(27)
piezo4 = OutputDevice(22)
piezo5 = OutputDevice(23)
piezo6 = OutputDevice(24)

buzz = Buzzer(16)
sensor = DistanceSensor(23,24)

while True:
    if sensor.distance < 0.23 and sensor.distance > 0.26:
        bz.off()
    else:
        bz.on()



