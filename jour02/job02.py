class Livre:
    # Constructor #
    def __init__(self, titre, auteur, nbPages):
        self.__titre = titre # private attribute
        self.__auteur = auteur # private attribute
        self.__nbPages = nbPages # private attribute

    # Getters and Setters #
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
    
    # The number of pages must be a positive integer #
    def set_nbPages(self, nbPages):
        if type(nbPages) == int:
            if nbPages > 0:
                self.__nbPages = nbPages
        else:
            print("The number of pages must be a positive integer")


# Test #
book1 = Livre("Les 4 accords toltèques", "Don Miguel Ruiz", 200)
book2 = Livre("Power of Now", "Eckhart Tolle", 300)
book3 = Livre("The Alchemist", "Paulo Coelho", 200)
            
print(book1.get_titre(), "by", book1.get_auteur(), "has", book1.get_nbPages(), "pages")
print(book2.get_titre(), "by", book2.get_auteur(), "has", book2.get_nbPages(), "pages")
print(book3.get_titre(), "by", book3.get_auteur(), "has", book3.get_nbPages(), "pages")


book1.set_nbPages(50)
book1.set_auteur("Joe Biden")
book1.set_titre("Everything to know to rule a country")

print(book1.get_titre(), "by", book1.get_auteur(), "has", book1.get_nbPages(), "pages")


book2.set_nbPages("50")
