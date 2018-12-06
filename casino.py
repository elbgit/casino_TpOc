# -*-coding:utf-8 -*

import os
import random

class Joueur:

    JOUEURS = []

    def __init__(self, nom, credit):
        self.nom = nom
        self.credit = credit
    
    def inscription_joueur(self):
        self.JOUEURS.append("toto")


class Roulette:
    def tirage(self):
        self.nombre = random.randrange(50)
        self.couleur = random.randrange(2)




joueur1 = Joueur(input("saisir nom : "), input("saisir crédit : ") )
roulette = Roulette()
roulette.tirage()
roulette.tirage()

print("bonjour " + joueur1.nom + " tu as un crédit de " + joueur1.credit)
print("nombre : " + str(roulette.nombre) + " couleur : " + str(roulette.couleur))
roulette.tirage()
print("nombre : " + str(roulette.nombre) + " couleur : " + str(roulette.couleur))


os.system("pause")