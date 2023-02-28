class Product:
    # Constructor #
    def __init__(self, name, priceHT, VAT):
        self.name = name
        self.priceHT = priceHT
        self.VAT = VAT

    # Methods #
    # Method to get the name attribute #
    def getName(self):
        return self.name
    
    # Method to get the priceHT attribute #
    def getPriceHT(self):
        return self.priceHT

    # Method to get the VAT attribute #
    def getVAT(self):
        return self.VAT

    # Method to calculate the price TTC #
    def CalculatePriceTTC(self):
        return self.priceHT * (1 + self.VAT/100)
    
    # Method to modify the name attribute #
    def modifyName(self, newName):
        self.name = newName
    
    # Method to modify the priceHT attribute #
    def modifyPriceHT(self, newPriceHT):
        self.priceHT = newPriceHT

    # Method to display the values of the attributes #
    def display(self):
        print("Name: ", self.name)
        print("Price HT: ", self.priceHT)
        print("VAT: ", self.VAT)
        print("Price TTC: ", self.CalculatePriceTTC())


# Creating three instances of the Product class with different values #
product1 = Product("\"Broken\" Smartphone", 150, 20)
product2 = Product("\"Broken\" Laptop", 400, 20)
product3 = Product("\"Broken\" TV", 500, 20)

print("Product 1:")
product1.display()

print("\nProduct 2:")
product2.display()

print("\nProduct 3:")
product3.display()

print(f"\nProduct:", product1.getName(),",Price TTC: ", product1.CalculatePriceTTC())
print(f"Product:", product2.getName(),",Price TTC: ", product2.CalculatePriceTTC())
print(f"Product:", product3.getName(),",Price TTC: ", product3.CalculatePriceTTC())

# Modifying the name and priceHT attributes of the product1 and product2 instances #
product1.modifyName("\"Fixed\" Smartphone")
product1.modifyPriceHT(600)

# Modifying the name and priceHT attributes of the product1 and product2 instances #
product2.modifyName("\"Fixed\" Laptop")
product2.modifyPriceHT(1200)

print("\nUpdated Product 1:")
product1.display()

print("\nUpdated Product 2:")
product2.display()

print(f"\nProduct:", product1.getName(),",Price TTC: ", product1.CalculatePriceTTC())
print(f"Product:", product2.getName(),",Price TTC: ", product2.CalculatePriceTTC())
print()
