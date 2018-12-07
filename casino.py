# -*-coding:utf-8 -*

import os
import random

credit = float(input("saisissez un crédit : "))
mise = float(input("saisissez votre mise : "))
gain = 0
jouer = 1

def croupier(nombre, couleur):
    nombre = random.randrange(50)
    couleur = random.randrange(2)
    return couleur * 100 + nombre

while credit > 0 and jouer == 1:
    
    credit = credit - mise + gain
    jouer = int(input("tapez 1 pour continuer, ou n'importe quoi pour arrêter"))
    

os.system("pause")