import random
from carte import Carte

class PaquetCartes:
    # Constructeur #
    # Création du paquet de cartes vide #
    def __init__(self):
        self.cartes = []

    # Ajout des cartes dans le paquet vide #
    def genererPaquet(self):
        for i in range(1, 14):
            for j in range(4):
                self.cartes.append(Carte(i, j))

    # Tirer une carte du paquet #    
    def tirer(self, iteration):
        cartes = []
        for i in range(iteration):
            carte = random.choice(self.cartes)
            self.cartes.remove(carte)
            cartes.append(carte)
        return cartes

    # Retourne le nombre de carte dans le paquet #
    def compteCartesRestante(self):
        return len(self.cartes)