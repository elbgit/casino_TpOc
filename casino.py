# -*-coding:utf-8 -*

import os
import random

while True:
    try:
        credit = int(input("saisissez votre crédit : "))
        break
    except ValueError:
        print("erreur de saisie")
        continue
    
gain = 0
jouer = 1

while credit > 0 and jouer == 1:
    print("votre crédit est de : " + str(credit))
    
    mise = int(input("saisissez votre mise : "))
    
    if mise > credit:
        while mise > credit:
            mise = float(input("saisissez une mise inférieure à votre crédit : "))
    
    ticket = int(input("faites-vos jeux ! "))
    if ticket > 50:
        while ticket > 50:
            ticket = int(input("choisissez un nombre entre 0 et 49 ! "))
    tirage = int(random.randrange(50))

    if tirage == ticket:
        gain = mise * 3
    elif (tirage % 2) == (ticket % 2):
        gain = (mise / 2)
    else:
        gain = 0

    credit = credit - mise + gain
    jouer = int(input("tapez 1 pour continuer, ou n'importe quoi pour arrêter"))
    

os.system("pause")