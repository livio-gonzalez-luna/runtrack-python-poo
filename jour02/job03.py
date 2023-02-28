class Livre:
    # Constructor #
    def __init__(self, titre, auteur, nbPages, disponible = True):
        self.__titre = titre # private attribute
        self.__auteur = auteur # private attribute
        self.__nbPages = nbPages # private attribute
        self.__disponible = disponible # private attribute

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

    # Methods #
    #  Method to check if the book is available or not #
    def verification(self):
        return self.__disponible
    
    # Method to borrow a book #
    def emprunter(self):
        if self.verification() == True:
            self.__disponible = False
            print("The book is borrowed successfully.")
        else:
            print("The book is not available to borrow.")

    # Method to return a book #
    def rendre(self):
        if self.verification() == False:
            print("The book is returned successfully.")
        else:
            self.__disponible = True
            print("The book is already available.")
    

# Test #
book1 = Livre("Les 42 accords toltèques", "Don Diego de la Vega", 1200)
print(book1.get_titre(), "de", book1.get_auteur(), "a", book1.get_nbPages(), "pages")

book1.verification()
book1.emprunter()
book1.verification()
book1.emprunter()
book1.rendre()
book1.verification()