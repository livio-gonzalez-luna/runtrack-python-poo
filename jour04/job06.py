# Créer une classe “Vehicule“ avec comme attribut une marque , une année et un prix.

# Créer la méthode “informationsVehicule“ qui écrit en console la marque, le modèle,
# l'année et le prix du véhicule.

# Créer la classe ”Voiture“ qui hérite de la classe ”Vehicule”. 

# Dans le constructeur de la classe Voiture, ajouter un attribut “portes” qui contient le nombre entier 4. 

# Créer dans cette classe , une méthode “informationsVehicule” qui affiche, en console, les
# informations générales du véhicule et le nombre de portes de la voiture.

# Instancier un objet, Voiture passer les attributs dont la classe a besoin et faites appel à
# la méthode “informationsVehicule”.

# Créer une classe Moto qui hérite de la classe “Vehicule” et ajouter l'attribut “roue” qui
# contient par défaut l’entier 2. Créer à nouveau une méthode “informationsVehicule”
# dans la classe Moto qui affiche l'intégralité des informations de la moto.

# Instancier un objet Moto et faites appel à la méthode informationsVehicule.

# Créer la méthode “demarrer” dans la classe Véhicule qui écrit en console “Attention, je
# roule”. Surcharger la méthode démarrer dans la classe Moto et Voiture afin d’afficher un
# message personnalisé. 

# Faites démarrer votre voiture et votre moto.

class Vehicule:
    # Constructeur #
    def __init__(self, marque, annee, prix):
        self.__marque = marque
        self.__annee = annee
        self.__prix = prix

    # Méthodes #
    # Informations Véhicule #
    def informationsVehicule(self):
        print("\nMarque: " + self.__marque)
        print("Année: " + str(self.__annee))
        print("Prix: " + str(self.__prix))

    # Démarrer #
    def demarrer(self):
        print("Attention, je roule")


class Voiture(Vehicule):
    # Constructeur #
    def __init__(self, marque, annee, prix):
        super().__init__(marque, annee, prix)
        self.__portes = 4

    # Méthodes #
    # Informations Véhicule #
    def informationsVehicule(self):
        super().informationsVehicule()
        print("Portes: " + str(self.__portes))

    # Démarrer #
    def demarrer(self):
        print("\nVroum vroum voiture")

class Moto(Vehicule):
    # Constructeur #
    def __init__(self, marque, annee, prix):
        super().__init__(marque, annee, prix)
        self.__roues = 2

    # Méthodes #
    # Informations Véhicule #
    def informationsVehicule(self):
        super().informationsVehicule()
        print("Roues: " + str(self.__roues))

    # Démarrer #
    def demarrer(self):
        print("\nVroum vroum vroum moto")

# Test #
voiture = Voiture("Tesla", 2020, 10000)
voiture.informationsVehicule()

moto = Moto("Yamaha", 2018, 5000)
moto.informationsVehicule()

voiture.demarrer()
moto.demarrer()