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
    if character == 'a':
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
#camera.capture('/home/pi/Documents/Capstone Project/program_code/test.png')       
#camera.stop_preview()


txt = tool.image_to_string(
    Image.open('/home/pi/Documents/Capstone Project/program_code/test.png'),
    lang="eng",
    builder=pyocr.builders.TextBuilder()
)
print(txt)
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



