# Créer une classe nommée “Forme” possédant une méthode nommée aire qui renvoie 0.

# Créer une classe “Rectangle” qui hérite de la classe “Forme” et qui possède deux
# attributs largeur et hauteur. Surcharger la méthode aire dans la classe Rectangle afin
# qu’elle ne renvoie plus 0, mais l’aire du rectangle.

# Imprimer en console le résultat de la méthode aire de la classe Rectangle.

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
    
rectangle = Rectangle(5, 10)
print(rectangle.aire())

