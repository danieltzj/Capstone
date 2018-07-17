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
    if character == ' ':
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

        piezo1.off()
        piezo2.off()
        piezo3.on()
        piezo4.on()
        piezo5.off()
        piezo6.off()
    elif character == '\\':
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
txt = 0

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

# Intialize GPIO
captureButton = Button(2)
playPauseButton = Button(3)
backButton = Button(4)

# Piezoeletric actuator layout corresponding to numbered piezo variables
# 1 4
# 2 5
# 3 6
piezo1 = OutputDevice(26)
piezo2 = OutputDevice(19)
piezo3 = OutputDevice(13)
piezo4 = OutputDevice(6)
piezo5 = OutputDevice(5)
piezo6 = OutputDevice(12)

# Buzzer and sensor
bz = Buzzer(16)
sensor = DistanceSensor(20,21) # echo, trigger                                                                                             

# turn off the buzzer first
bz.on()

# States
currentState = 0
idleState = 0
captureState = 1
outputState = 2
pauseState = 3

def capture_and_convert():
    camera.capture('/home/pi/Capstone/test.png')

    txt = tool.image_to_string(
        Image.open('/home/pi/Capstone/test.png'),
        lang="eng",
        builder=pyocr.builders.TextBuilder()
    )
    print(txt)
    return txt
    # txt is a Python string
    

# Main Program Loop
while(True):
    # wait for the capture button to be pressed to start the sensor
    # Buzz when the text is in the distance threshold of the camera
    captureButton.wait_for_press()
    currentState = captureState
    print("Capture button pressed!")
    while(currentState == 1):
        print(sensor.distance)
        while sensor.distance > 0.22 and sensor.distance < 0.24:
            bz.beep()
            if captureButton.is_held:
                txt = capture_and_convert()
                print("Picture taken")
                currentState = outputState
                break
        sleep(1)

    # Start outputting Braille
    i = 0 # counter for which character
    
    # Error handling on OCR on picture
    try:
        # For testing purposes
        # print the whole translated text
        print("The translated text is ")
        print(txt)

        while( i < len(txt)):
            print(txt[i])
            convert(txt[i])
            sleep(0.4)
            if playPauseButton.is_pressed and currentState == outputState:
                print("Output Paused")
                currentState = pauseState

                while currentState == pauseState:
                    # if the play/pause button is pressed, go back to the output state
                    # to resume outputting braile for either the same or new index in the translated string
                    if playPauseButton.is_held:
                        print("Output Restarted")
                        currentState = outputState
                    # Whenever back button is pressed in this state, it will go back a single character
                    # no change in current state as it's still in the pause state
                    elif backButton.is_pressed:
                        i = i-1
                        convert(txt[i])
                        sleep(0.4)
                        print("Moved back to character ", txt[i], "from character ", txt[i+1])
            i = i + 1
        # Once finished outputting, go back to idle state
        print("Text has finished outputting")
        currentState = idleState
    # Handle the exception of untranslatable picture
    # Go back to idle state
    except:
        # 2 beeps to indicate an exception
        print("There was a problem translating the picture, please try again")
        bz.beep(2)
        currentState = idleState

#camera.start_preview()
#sleep(10)
#camera.stop_preview()
