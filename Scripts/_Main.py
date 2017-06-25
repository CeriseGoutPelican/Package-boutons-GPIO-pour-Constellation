import Constellation
from button import *
import time

""" FONCTION : setup
    ================
    Permet de démarer l'écoute des boutons sur les ports GPIO en entrée

    PARAMETRES
    ==========
    pins : liste d'entiers contenant les numéros des pins à écouter

"""
def setup(pins):
    GPIO.setmode(GPIO.BCM)
        
    for i in range(len(pins)):
        Constellation.WriteInfo("Début de l'écoute du bouton %i" % pins[i])
		pins[i] = Button(pins[i]) 
		pins[i].addXButtonListener(onButtonEvent)

""" FONCTION : onButtonEvent
    ========================
    Fonction de callback d'un bouton utilisée par la bilbiothèque button.py (voir le fichier pur référence)
"""
def onButtonEvent(button, event):
    if event == BUTTON_LONGPRESSED:
		Constellation.WriteInfo("Bouton %i clique longuement" % button.buttonPin)
    elif event == BUTTON_CLICKED:
        Constellation.WriteInfo("Bouton %i clique simplement" % button.buttonPin)
    elif event == BUTTON_DOUBLECLICKED:
		Constellation.WriteInfo("Bouton %i double clique" % button.buttonPin)

""" PROGRAMME PRINCIPAL
    ===================
"""
def OnStart():

    Constellation.WriteInfo("Démarage du packet Boutons...")
    # On écoute les boutons suivants :
    setup([13,19,16,20,21])
    
    pass

Constellation.Start()