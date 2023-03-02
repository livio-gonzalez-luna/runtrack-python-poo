class Carte:
    # Constructeur #
    # Création des attributs qui définissent une carte #
    def __init__(self,valeur,couleur):
        self.val = valeur
        self.carte = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'][valeur-1]
        self.couleur = '♥♦♣♠'[couleur]
    
    # Methodes #
    # Affiche la carte #
    def printCarte(self):
        print('┌───────┐')
        print(f'│ {self.carte:<2}    │')
        print('│       │')
        print(f'│   {self.couleur}   │')
        print('│       │')
        print(f'│    {self.carte:>2} │')
        print('└───────┘') 

    # Retourne la valeur de la carte #
    def valeur(self):
        if self.val >= 10:
            return 10
        elif self.val == 1:
            return 11
        return self.val
    
