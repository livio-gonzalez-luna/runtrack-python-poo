class Commande:
    # Constructor #
    def __init__(self, numCommande, listPlats, statutCommande = "En cours"):
        self.__numCommande = numCommande
        self.__listPlats = listPlats
        self.__statutCommande = statutCommande

    # Getters and Setters #
    def get_numCommande(self):
        return self.__numCommande
    
    def set_numCommande(self, numCommande):
        self.__numCommande = numCommande

    def get_listPlats(self):
        return self.__listPlats
    
    def set_listPlats(self, listPlats):
        self.__listPlats = listPlats

    def get_statutCommande(self):
        return self.__statutCommande

    def set_statutCommande(self, statutCommande):
        self.__statutCommande = statutCommande

    # Publics Methods #
    # Method to add a dish to the order #
    def add_dish(self, dish, price):
        self.__listPlats[dish] = price

    # Method to cancel an order #
    def cancel_order(self):
        self.__statutCommande = "Annulée"

    # Method to finish an order #
    def finish_order(self):
        self.__statutCommande = "Terminée"


    # Private methods #
    # Method to calculate the total of an order #
    def __calculate_total(self):
        total = 0
        for plat in self.__listPlats:
            total += self.__listPlats[plat]
        return total
    
    # Method to calculate the TVA #
    def __calculate_tva(self):
        return self.__calculate_total() * 0.2
    
    # Method to calculate the total TTC #
    def __calculate_total_ttc(self):
        return self.__calculate_total() * 1.2

    # Method to display an order #
    def display_order(self):
        if self.__statutCommande == "Annulée":
            print("\nLa commande", self.__numCommande, "est", self.__statutCommande, ".")

        elif self.__statutCommande == "Terminée":
            print("\nLa commande", self.__numCommande, "est", self.__statutCommande, 
                "\nElle contient les plats suivants: ",self.__listPlats, 
                "\nSon total de", self.__calculate_total(), "€.", 
                "\nLa TVA est de", self.__calculate_tva(), "€.",
                "\nLe total TTC est de", self.__calculate_total_ttc(), "€.")  
        else:
            print("\nLa commande", self.__numCommande, "est", self.__statutCommande, 
                "\nElle contient les plats suivants: ",self.__listPlats, 
                "\nSon total de", self.__calculate_total(), "€.", 
                "\nLa TVA est de", self.__calculate_tva(), "€.",
                "\nLe total TTC est de", self.__calculate_total_ttc(), "€.")

# Test #

# Create a list of dishes for first order#
listPlats1 = {
    "Pizza" : 10,
    "Pâtes" : 8
}

# Create an order #
order1 = Commande(1, listPlats1)
order1.display_order()
# Add a dish to the order #
order1.add_dish("Salade", 5)
order1.display_order()

# Finish the order #
order1.finish_order()
order1.display_order()

# Cancel the order #
order1.cancel_order()
order1.display_order()

# Create a list of dishes for the second order#
listPlats2 = {
    "Sandwich" : 5,
    "Salade" : 5,
    "Frites" : 3
}

# Create an order #
order2 = Commande(2, listPlats2)
order2.display_order()

# Finish the order #
order2.finish_order()
order2.display_order()
