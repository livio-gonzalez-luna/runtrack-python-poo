class Croupier:
    # Constructeur #
    def __init__(self):
        self.__main = []

    # Méthodes #
    # Main #
    def main(self):
        return self.__main

    # Ajouter Carte #
    def ajouterCarte(self, carte):
        self.__main.append(carte)

    # Afficher Main #
    def afficherMain(self):
        for carte in self.__main:
            carte.afficher()

    # Calculer Score #
    def calculerScore(self):
        score = 0
        for carte in self.__main:
            if carte.valeur() == "As":
                score += 1
            elif carte.valeur() == "Valet" or carte.valeur() == "Dame" or carte.valeur() == "Roi":
                score += 10
            else:
                score += int(carte.valeur())
        return score

    # Afficher Score #
    def afficherScore(self):
        print("Croupier : " + str(self.calculerScore()))

    # Est Gagnant #
    def estGagnant(self, joueur):
        if self.calculerScore() > joueur.calculerScore() and self.calculerScore() <= 21:
            return True
        else:
            return False

    # Est Perdant #
    def estPerdant(self, joueur):
        if self.calculerScore() > 21 or self.calculerScore() < joueur.calculerScore():
            return True
        else:
            return False

    # Est Egalite #
    def estEgalite(self, joueur):
        if self.calculerScore() == joueur.calculerScore():
            return True
        else:
            return False

    # Est Fini #
    def estFini(self):
        if self.calculerScore() >= 17:
            return True
        else:
            return False

    # Prendre Carte #
    def prendreCarte(self, paquet):
        self.ajouterCarte(paquet.distribuer())