# Package boutons GPIO pour Constellation
Le package permet d'écouter les pins GPIO de votre Raspeberry Pi et de renvoyer une information sous forme de message Callback contenant un json avec le numéro du pin `pinNumber` ainsi que son utilisation `status` contenant trois valeurs possibles : 
 * `clicked` : le bouton a été cliqué 
 * `doubleClicked` : le bouton a été double cliqué
 * `longClicked` : le bouton a été cliqué longement

## Installation
Une seule dépendance est nécessaire pour une utilisation correcte du module : [RPi.GPIO](https://sourceforge.net/p/raspberry-gpio-python/wiki/install/). Le module s'installe simplement ainsi : 
```
$ sudo apt-get update
$ sudo apt-get install python-rpi.gpio
```

## Usage
Pour utiliser les informations reçues par les boutons, il est nécessaire de s'abonner au message Callback de la manière suivante :
```python
@Constellation.MessageCallback()
def ButtonAction(data):
    "Action et description d'un bouton poussoir branché sur un port GPIO du RPi poussé par packet ButtonRPi"

    BUTTON_HOME     = 19

    # Clics simples
    if data.event == "clicked":
        if data.pin == BUTTON_HOME:
            pass
    # Clics doubles
    elif data.event == "doubleclicked":
        if data.pin == BUTTON_HOME:
            pass
    # Clics longs 
    elif data.event == "longpressed":
        if data.pin == BUTTON_HOME:
            pass
```
