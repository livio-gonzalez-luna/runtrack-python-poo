class Personne:
    # Constructeur #
    def __init__(self, age=14):
        self.age = age

    # Méthodes #
    # Afficher age #
    def afficherAge(self):
        print(self.age)

    # Bonjour #
    def bonjour(self):
        print("Hello")

    # Modifier age #
    def modifierAge(self, age):
        self.age = age

# Création d'un objet qui hérite de la classe Personne #
class Eleve(Personne):
    # Aller en cours #
    def allerEnCours(self):
        print("Je vais en cours")

    # Afficher age #
    def affichageAge(self):
        print("J'ai", self.age, "ans")

# Création d'un objet qui hérite de la classe Personne #
class Professeur(Personne):
    # Constructeur #
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee
    # Enseigner #
    def enseigner(self):
        print("Le cours va commencer")

    # Afficher matière #
    def afficherMatiere(self):
        print(self.__matiereEnseignee)

p = Personne()
p.bonjour()

e = Eleve()
e.affichageAge()
e.afficherAge()
