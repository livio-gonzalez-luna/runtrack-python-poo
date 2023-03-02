# Créer une classe “Rectangle” avec comme attribut privé longueur et largeur. 

# Créer la méthode “périmètre” permettant de calculer le périmètre du rectangle ainsi que la
# méthode “surface“ permettant de calculer la surface du rectangle.

# Créer les accesseurs et mutateurs permettant de manipuler les attributs de la classe.

# Créer une classe “Parallélépipède“ héritant de la classe Rectangle avec en plus un
# attribut hauteur et une autre méthode volume permettant de calculer le volume du
# parallélépipède.

# Instancier la classe Rectangle et assurez-vous que toutes les méthodes fonctionnent.

class Rectangle:
    # Constructeur #
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # Méthodes #
    # Périmètre #
    def perimetre(self):
        return (self.__longueur + self.__largeur) * 2

    # Surface #
    def surface(self):
        return self.__longueur * self.__largeur

    # Accesseurs #
    # Longueur #
    def getLongueur(self):
        return self.__longueur

    # Largeur #
    def getLargeur(self):
        return self.__largeur

    # Mutateurs #
    # Longueur #
    def setLongueur(self, longueur):
        self.__longueur = longueur

    # Largeur #
    def setLargeur(self, largeur):
        self.__largeur = largeur


class Parallelepipede(Rectangle):
    # Constructeur #
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    # Méthodes #
    # Volume #
    def volume(self):
        return self.surface() * self.__hauteur

    # Accesseurs #
    # Hauteur #
    def getHauteur(self):
        return self.__hauteur

    # Mutateurs #
    # Hauteur #
    def setHauteur(self, hauteur):
        self.__hauteur = hauteur


# Test #
rectangle = Rectangle(10, 5)
print(rectangle.perimetre())
print(rectangle.surface())

parallelepipede = Parallelepipede(10, 5, 2)
print(parallelepipede.volume())
