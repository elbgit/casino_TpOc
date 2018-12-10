# -*-coding:utf-8 -*

import os
import random
import math

while True:
    try:
        credit = int(input("saisissez votre crédit : "))
        if credit < 1:
            raise ValueError("valeur négative ou nulle")
        break
    except ValueError:
        print("erreur de saisie")
        continue
    
gain = 0
jouer = 1

while credit > 0 and jouer == 1:
    print("ici votre crédit est de : " + str(credit))
    
    while True:
        try:
            mise = int(input("saisissez votre mise : "))
            if mise < 1:
                raise ValueError("mise inférieure à 1")
            break
        except ValueError:
            print("erreur de saisie")
            continue
    
    if mise > credit:
        while mise > credit:
            while True:
                try:
                    mise = float(input("saisissez une mise inférieure à votre crédit : "))
                    if mise < 1:
                        raise ValueError("Mise inférieure à 1")
                    break
                except ValueError:
                    print("erreur de saisie")
                    continue
    while True:
        try:
            ticket = int(input("faites-vos jeux ! "))
            break
        except ValueError:
            print("erreur de saisie")
            continue
        
    if ticket > 50 or ticket < 0:
        while ticket > 50 or ticket < 0:
            while True:
                try:
                    ticket = int(input("choisissez un nombre entre 0 et 49 ! "))
                    break
                except ValueError:
                    print("erreur de saisie")
                    continue
                
    tirage = int(random.randrange(50))
    print(str(tirage) + " " + ("pair" if tirage % 2 == 0 else "impair"))

    if tirage == ticket:
        gain = math.ceil(mise * 3)
    elif (tirage % 2) == (ticket % 2):
        gain = math.ceil((mise / 2))
    else:
        gain = 0
    
    credit = credit - mise + gain
    print("votre crédit est épuisé. Fin du jeu") if credit == 0 else print("votre crédit est de : " + str(credit) + "$ et votre gain est de : " + str(gain) + "$")
    
    try:
        if credit > 0:
            jouer = int(input("tapez 1 pour continuer, ou n'importe quoi pour arrêter"))
        else:
            jouer = 0
    except ValueError:
        jouer = 0
    

os.system("pause")