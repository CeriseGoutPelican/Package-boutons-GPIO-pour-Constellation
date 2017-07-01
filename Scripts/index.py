import Constellation
import RPi.GPIO as GPIO
import time
from buttonlib import *

""" FONCTION : onButtonEvent
    ========================
    Fonction de callback d'un bouton utilisée par la bilbiothèque button.py (voir le fichier pur référence)
"""
def onButtonEvent(button, event):

    if event == BUTTON_LONGPRESSED:
        Constellation.SendMessage("ConstellationReveilISEN", "ButtonAction", {"pin":button.buttonPin, "event":"longpressed"}, Constellation.MessageScope.package)
    elif event == BUTTON_CLICKED:
        Constellation.SendMessage("ConstellationReveilISEN", "ButtonAction", {"pin":button.buttonPin, "event":"clicked"}, Constellation.MessageScope.package)
    elif event == BUTTON_DOUBLECLICKED:
        Constellation.SendMessage("ConstellationReveilISEN", "ButtonAction", {"pin":button.buttonPin, "event":"doubleclicked"}, Constellation.MessageScope.package)

def OnExit():
    Constellation.WriteInfo("Fermeture du packet Constellation bouton simples...")
    GPIO.cleanup()

""" PROGRAMME PRINCIPAL
    ===================
"""
def OnStart():

    # Démarrage du packet 
    Constellation.WriteInfo("Démarrage du packet Boutons...")
    Constellation.OnExitCallback = OnExit

    # Settings GPIO
    Constellation.WriteInfo("Setmode GPIO...")
    GPIO.setmode(GPIO.BCM)

    # Récupération des PINS dans la configuration
    #dynamic json = Constellation.GetSettingAsJsonObject("listening_pins");
    #Constellation.WriteInfo(json.Boolean);
       
    pins = [13,16,19,20,26]

    # Début de l'écoute
    for i in pins:
        Constellation.WriteInfo("Début de l'écoute du bouton %i" % i)
        bt = Button(i) 
        bt.addXButtonListener(onButtonEvent)

    pass

Constellation.Start(OnStart)