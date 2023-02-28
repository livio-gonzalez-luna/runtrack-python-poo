class Livre:
    def __init__(self, titre, auteur, nbPages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbPages = nbPages

    def get_titre(self):
        return self.__titre
    
    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur
    
    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nbPages(self):
        return self.__nbPages
    
    def set_nbPages(self, nbPages):
        if nbPages < 0 and == int:
            print("Le nombre de pages doit être supérieur à 0.")
        else:
            self.__nbPages = nbPages