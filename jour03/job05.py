import random
import time

class Personnage:
    # Constructeur #
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    # Méthodes #
    # Attaque #
    def attaquer(self, adversaire):
        print(self.nom, "attaque comme il peut", adversaire.nom)
        adversaire.vie -= 1

    # Soin #
    def soin(self):
        print(self.nom, "boit une potion de soin")
        self.vie += 2

    # Bouclier #
    def bouclier(self):
        print(self.nom, "utilise un bouclier")
        self.vie += 1

    # Chute #
    def chute(self):
        print(self.nom, "tombe dans un trou")
        self.vie -= 1

    # Double attaque #
    def doubleAttaque(self, adversaire):
        print(self.nom, "utilise une double attaque sur", adversaire.nom)
        adversaire.vie -= 2

    # Attaque spéciale #
    def attaqueSpeciale(self, adversaire):
        print(self.nom, "utilise une attaque spéciale sur", adversaire.nom)
        if self.nom == "Joueur":
            adversaire.vie -= 3
        else:
            self.vie -= 3

    # Afficher vie #
    def afficherVie(self):
        print(self.nom, "a", self.vie, "points de vie")

    # Jouer tour #
    def jouerTour(self, adversaire):
        choix = random.randint(1, 6)
        if choix == 1:
            self.attaquer(adversaire)
        elif choix == 2:
            self.soin()
        elif choix == 3:
            self.doubleAttaque(adversaire)
        elif choix == 4:
            self.attaqueSpeciale(adversaire)
        elif choix == 5:
            self.bouclier()
        elif choix == 6:
            self.chute()

# Jeu #
class Jeu:
    # Constructeur #
    def __init__(self):
        self.niveau = 0

    # Méthodes #
    # Choisir niveau #
    def choisirNiveau(self):
        self.niveau = int(input("Choisissez un niveau de difficulté : "))
        if self.niveau == 1:
            self.niveau = 10
        
        elif self.niveau == 2:
            self.niveau = 20
        
        elif self.niveau == 3:
            self.niveau = 30

    # Lancer jeu #
    def lancerJeu(self):
        self.choisirNiveau()
        turn = random.randint(1, 2)
        joueur1 = Personnage("Joueur 1", self.niveau)
        joueur2 = Personnage("Joueur 2", self.niveau)
        while joueur1.vie > 0 and joueur2.vie > 0:
            if turn == 1:
                joueur1.jouerTour(joueur2)
            else:
                joueur2.jouerTour(joueur1)
            joueur1.afficherVie()
            joueur2.afficherVie()
            print()
            time.sleep(0.5)
        if joueur1.vie > joueur2.vie:
            print("Joueur1 a gagné !")
        else:
            print("Joueur2 a gagné !")

jeu = Jeu()
jeu.lancerJeu()
