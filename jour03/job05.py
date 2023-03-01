# Commencer par créer une classe nommée Personnage prenant des paramètres de
# construction : nom (string) et vie(int).

# Créez au minimum une méthode “attaquer” qui enlève des points à son adversaire.

# Ensuite créer la classe “Jeu” ne prenant pas de paramètre.

# Créer une méthode “choisirNiveau” qui permet de demander au joueur le niveau de difficulté. Celui-ci sera
# stocké dans l’attribut niveau.
# En fonction du niveau choisi, le nombre de points de vie du joueur ainsi que de l'ennemi
# seront différents.

# Créer “lancerJeu”, méthode qui utilise l’attribut niveau. Cette méthode aura pour but
# d’instancier deux objets “Personnage”, un qui représente le joueur et l’autre l'ennemi
# avec un nombre de points défini en fonction du niveau.

# Implémenter le déroulement d’une partie en demandant au joueur le niveau de difficulté
# et pensez à ajouter une méthode qui vérifie la santé de vos personnages ainsi qu’une
# méthode permettant de vérifier qui a gagné.


class Personnage:
    def __init__(self, nom : str, vie : int):
        self.nom = nom
        self.vie = vie

    def attaquer(self, ennemi):
        ennemi.vie -= 1

class Jeu:
    def __init__(self):
        self.niveau = 0

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez un niveau de difficulté (1, 2 ou 3) : "))

    def lancerJeu(self):
        self.choisirNiveau()
        if self.niveau == 1:
            joueur = Personnage("Joueur", 10)
            ennemi = Personnage("Ennemi", 10)
        elif self.niveau == 2:
            joueur = Personnage("Joueur", 20)
            ennemi = Personnage("Ennemi", 20)
        elif self.niveau == 3:
            joueur = Personnage("Joueur", 30)
            ennemi = Personnage("Ennemi", 30)
        else:
            print("Niveau invalide")
            return

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            ennemi.attaquer(joueur)

        if joueur.vie > 0:
            print("Le joueur a gagné")
        else:
            print("L'ennemi a gagné")

        def verifierSante(self):
            if self.vie <= 0:
                print("Le personnage est mort")
