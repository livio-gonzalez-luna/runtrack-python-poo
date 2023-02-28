class Voiture:
    # Constructor #
    def __init__(self, marque, modele, annee, kilometrage, en_marche = False, reservoir = 50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir

    # Getters and Setters #
    def get_marque(self):
        return self.__marque
    
    def set_marque(self, marque):
        self.__marque = marque

    def get_modele(self):
        return self.__modele

    def set_modele(self, modele):
        self.__modele = modele

    def get_annee(self):
        return self.__annee
    
    def set_annee(self, annee):
        self.__annee = annee

    def get_kilometrage(self):
        return self.__kilometrage

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def get_en_marche(self):
        return self.__en_marche
    
    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche

    def get_reservoir(self):
        return self.__reservoir
    
    # Methods #
    # Method to start the car #
    def demarrer(self):
        if self.__en_marche == True:
            print("La voiture est déjà en marche.")
        elif self.__reservoir > 5:
            self.__en_marche = True
        else:
            print("\nLa voiture", self.__marque, self.__modele, self.__annee, "ne peut pas démarrer, pas assez d' essence.")
            print("Le réservoir contient", self.__reservoir, "litres.")

    # Method to stop the car #
    def arreter(self):
        self.__en_marche = False

    # Method to display "voiture" informations #
    def info_car(self):
        print("\nLa voiture est une", self.__marque, self.__modele, "de l'année", self.__annee, "avec un kilométrage de", self.__kilometrage, "km.")
        print("Le réservoir contient", self.__reservoir, "litres.")
        if self.__en_marche == True:
            print("La voiture est en marche.")
        else:
            print("La voiture est arrêtée.")




# Test #
car1 = Voiture("BMW", "X5", 2019, 65000)
car2 = Voiture("Audi", "A4", 2018, 10000, reservoir = 120)
car3 = Voiture("Mercedes", "GLA", 2018, 1200, reservoir = 4)


car1.info_car()
car2.info_car()
car3.info_car()

car1.demarrer()
car2.demarrer()
car3.demarrer()

car1.info_car()
car2.info_car()
car3.info_car()

