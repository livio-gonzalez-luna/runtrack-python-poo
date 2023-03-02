# Récupérer votre classe “Forme” crée juste au-dessus.

# Créer une classe fille nommée “Cercle” qui hérite de la classe “Forme” et possédant un
# attribut radius.

# Surcharger la méthode “aire” dans la classe Cercle pour qu'elle renvoie l’aire du cercle.

# Créez une instance de chaque classe Rectangle et Cercle et utilisez-les pour tester les
# différentes surcharges de la méthode aire en affichant les résultats en console.

class Forme:
    # Méthodes #
    # Aire #
    def aire(self):
        return 0
    
class Rectangle(Forme):
    # Constructeur #
    def __init__(self, largeur, hauteur):
        self.__largeur = largeur
        self.__hauteur = hauteur

    # Méthodes #
    # Aire #
    def aire(self):
        return self.__largeur * self.__hauteur
    
class Cercle(Forme):
    # Constructeur #
    def __init__(self, radius):
        self.__radius = radius

    # Méthodes #
    # Aire #
    def aire(self):
        return 3.14 * self.__radius ** 2

# Test #    
rectangle = Rectangle(5, 10)
print(rectangle.aire())

cercle = Cercle(5)
print(cercle.aire())