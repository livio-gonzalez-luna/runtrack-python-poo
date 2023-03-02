# À l’aide de la classe “Personne” , Eleve et Professeur écrit au-dessus, faites dire bonjour
# à votre élève grâce à la méthode “bonjour” ainsi que “je vais en cours” grâce à la
# méthode “allerEnCours”. Redéfinir l’age de l’élève à 15 ans.
# Créer un objet Professeur, 40 ans, faite dire bonjour à votre professeur et commencer le
# cours grâce à la méthode enseigner.

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
        print("Le cours va commencer avec la matière", self.__matiereEnseignee, "")

    # Afficher matière #
    def afficherMatiere(self):
        print(self.__matiereEnseignee)

eleve = Eleve()
eleve.bonjour()
eleve.allerEnCours()
eleve.modifierAge(15)
eleve.affichageAge()

professeur = Professeur("Mathématiques")
professeur.modifierAge(40)

professeur.bonjour()
professeur.enseigner()