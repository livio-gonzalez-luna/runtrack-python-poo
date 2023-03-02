from paquet import PaquetCartes
from joueur import Joueur

class Blackjack:
    # Constructeur #
    def __init__(self):
        self.paquetCartes = PaquetCartes()
        self.paquetCartes.genererPaquet()
        self.joueur = Joueur(False, self.paquetCartes)
        self.croupier = Joueur(True, self.paquetCartes)

    # Méthodes #
    # Jouer une partie #
    def jouer(self):
        # Générer les mains #
        joueurStatus = self.joueur.genereMain()
        croupierStatus = self.croupier.genereMain()

        # Afficher les cartes #
        self.croupier.displayCartes()
        self.joueur.displayCartes()
        
        # Vérifier le statut des mains #
        if joueurStatus == 1:
            print("Blackjack pour le joueur! Felicitations!")
            if croupierStatus == 1:
                print("Egalité des mains. Bonne chance la prochaine fois!")
            return 1

        choix = ""
        while choix != "s":
            bust = 0
            choix = input("Prendre une carte(p) ou stop(s)? ")

            if choix == "p":
                bust = self.joueur.prendreUneCarte()
                self.joueur.displayCartes()
            if bust == 1:
                print("Joueur a dépassé la limite de 21!")
                return 1
        print("\n")
        self.croupier.displayCartes()
        if croupierStatus == 1:
            print("Blackjack pour le dealer!")
            return 1

        # Croupier tire #
        while self.croupier.checkScore() < 17:
            if self.croupier.prendreUneCarte() == 1:
                self.croupier.displayCartes()
                print("Le croupier a dépassé la limite de 21!")
                return 1
            self.croupier.displayCartes()

        if self.croupier.checkScore() == self.joueur.checkScore():
            print("Egalité des mains. Bonne chance la prochaine fois!")
        elif self.croupier.checkScore() > self.joueur.checkScore():
            print("Le croupier gagne!")
        elif self.croupier.checkScore() < self.joueur.checkScore():
            print("Le joueur gagne, félicitations!")

b = Blackjack()
b.jouer()