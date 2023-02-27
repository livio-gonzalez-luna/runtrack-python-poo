import math

class Cercle:
    # Constructor #
    def __init__(self, rayon):
        self.rayon = rayon
    
    # Methods #

    # Metthod to change the value of the rayon attribute #
    def changerRayon(self, nouveauRayon):
        self.rayon = nouveauRayon
        
    # Method to calculate the circonference #
    def circonference(self):
        return 2 * math.pi * self.rayon
    
    # Method to calculate the area #
    def aire(self):
        return math.pi * self.rayon ** 2
    
    # Method to calculate the diameter #
    def diametre(self):
        return 2 * self.rayon
    
    # Method to display the values of the attributes #
    def afficherInfos(self):
        print(f"Rayon: {self.rayon}")
        print(f"Circonférence: {self.circonference()}")
        print(f"Aire: {self.aire()}")
        print(f"Diamètre: {self.diametre()}")

# Creating two instances of the Cercle class with different values #
cercle1 = Cercle(4)
cercle2 = Cercle(7)

# Testing the methods of the Cercle class #
cercle1.afficherInfos()
print()
cercle2.afficherInfos()
