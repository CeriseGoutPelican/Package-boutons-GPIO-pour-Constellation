from button import *
import RPi.GPIO as GPIO
import time
import select

def setup(pins):
    GPIO.setmode(GPIO.BCM)
        
    for i in range(len(pins)):
		pinBuffer = pins[i]
		pins[i] = Button(pins[i]) 
		pins[i].addXButtonListener(onButtonEvent)

def onButtonEvent(button, event):
    global isRunning
	
    if event == BUTTON_LONGPRESSED:
		print "Bouton %i clique longuement" % button.buttonPin 
    elif event == BUTTON_CLICKED:
        print "Bouton %i clique simplement" % button.buttonPin 
    elif event == BUTTON_DOUBLECLICKED:
		print "Bouton %i double clique" % button.buttonPin 
       
setup([13,19,16,20,21])

# Le select permet d'eviter que le programme ne se ferme	
select.select([],[],[])
GPIO.cleanup()

