from paquet import PaquetCartes

class Joueur:
    # Constructeur #
    def __init__(self, croupier, paquet):
        self.cartes = []
        self.croupier = croupier
        self.paquet = paquet
        self.score = 0

    # Méthodes #
    # Prendre une carte du paquet #
    def prendreUneCarte(self):
        self.cartes.extend(self.paquet.tirer(1))
        self.checkScore()
        if self.score > 21:
            return 1
        return 0

    # Tirer une carte du paquet #
    def genereMain(self):
        self.cartes.extend(self.paquet.tirer(2))
        self.checkScore()
        if self.score == 21:
            return 1
        return 0

    # Vérifier le score du joueur #
    def checkScore(self):
        compteur = 0
        self.score = 0
        for c in self.cartes:
            if c.valeur() == 11:
                compteur += 1
            self.score += c.valeur()

        while compteur != 0 and self.score > 21:
            compteur -= 1
            self.score -= 10
        return self.score

    # Afficher les cartes du joueur #
    def displayCartes(self):
        if self.croupier:
            print("Cartes du croupier")
        else:
            print("Cartes du joueur")

        for i in self.cartes:
            i.printCarte()


        print("Score: " + str(self.score))

