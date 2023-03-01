class Joueur:
    # Constructor #
    def __init__(self, nom, numero, position, buts, passes, jaunes, rouges):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = buts
        self.passes = passes
        self.jaunes = jaunes
        self.rouges = rouges

    # Methods #
    # Method to add a goal #
    def marquerUnBut(self):
        self.buts += 1

    # Method to add a pass #
    def effectuerUnePasseDecisive(self):
        self.passes += 1

    # Method to add a yellow card #
    def recevoirUnCartonJaune(self):
        self.jaunes += 1

    # Method to add a red card #
    def recevoirUnCartonRouge(self):
        self.rouges += 1

    # Method to display the statistics of a player #
    def afficherStatistiques(self):
        print("\nNom : ", self.nom)
        print("Numero : ", self.numero)
        print("Position : ", self.position)
        print("Buts : ", self.buts)
        print("Passes : ", self.passes)
        print("Cartons jaunes : ", self.jaunes)
        print("Cartons rouges : ", self.rouges)


class Equipe:
    # Constructor #
    def __init__(self, nom, joueurs=[]):
        self.nom = nom
        self.joueurs = joueurs


    # Methods #
    # Method to add a player to the team #
    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    # Method to remove a player from the team #
    def afficherStatistiquesJoueurs(self):
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

    # Method to update the statistics of a player #
    def mettreAJourStatistiquesJoueur(self, joueur, buts, passes, jaunes, rouges):
        joueur.buts += buts
        joueur.passes += passes
        joueur.jaunes += jaunes
        joueur.rouges += rouges


# Test #
joueur1 = Joueur("Ronaldo", 7, "Attaquant", 0, 0, 0, 0)
joueur2 = Joueur("Messi", 10, "Attaquant", 0, 0, 0, 0)
joueur3 = Joueur("Neymar", 11, "Attaquant", 0, 0, 0, 0)
joueur4 = Joueur("Mbappe", 9, "Attaquant", 0, 0, 0, 0)
joueur5 = Joueur("Kante", 7, "Milieu", 0, 0, 0, 0)
joueur6 = Joueur("Pogba", 6, "Milieu", 0, 0, 0, 0)
joueur7 = Joueur("Varane", 4, "Defenseur", 0, 0, 0, 0)
joueur8 = Joueur("Lloris", 1, "Gardien", 0, 0, 0, 0)

equipe1 = Equipe("France")

equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe1.ajouterJoueur(joueur3)
equipe1.ajouterJoueur(joueur4)
equipe1.ajouterJoueur(joueur5)
equipe1.ajouterJoueur(joueur6)
equipe1.ajouterJoueur(joueur7)
equipe1.ajouterJoueur(joueur8)

equipe1.afficherStatistiquesJoueurs()

joueur1.marquerUnBut()
joueur1.effectuerUnePasseDecisive()
joueur1.recevoirUnCartonJaune()

equipe1.mettreAJourStatistiquesJoueur(joueur1, 1, 1, 1, 0)

joueur1.afficherStatistiques()
