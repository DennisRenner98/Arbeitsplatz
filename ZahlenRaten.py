# ZahlenRatenAufgabe

import random

x = random.randint(0, 100)

eingabe = -0
# Eingabe wird angegeben, um die while Schleife überhaupt möglich zu machen
# als 0 liegt sie außerhalb des möglichen Bereiches, um Überschneidungen zu vermeiden

print("Ich habe eine zufällige Zahl zwischen 0 und 100 generiert. \nVersuch sie zu erraten!")
while eingabe != x:

    eingabe = int(input())
    # Eingabe einer beliebigen ganzen Zahl wird gefordert

    if eingabe > x:
        print("Leider daneben. Probier's mit einer niedrigeren Zahl!")

    elif eingabe < x:
        print("Leider daneben. Probier's mit einer höheren Zahl!")

    else:
        print("Spitze! Du hast die Zahl erraten!")
        # Eingegebene Zahl wird mit x verglichen
        
