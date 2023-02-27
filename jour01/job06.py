class Animal:
    def __init__(self):
        self.age = 0
        self.name = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, name):
        self.name = name

# Instantiate an object of the Animal class
animal = Animal()

# Print the age attribute of the animal object
print("L'age de l'animal est:", animal.age)

# Call the "vieillir" method of the animal object 
animal.vieillir()

# Print the age attribute of the animal object that it has been updated
print("L'age de l'animal est:", animal.age)

# Call the "nommer" method of the animal object
animal.nommer("Loki")

# Print the name attribute of the animal object that it has been updated
print("L'animal se nomme:", animal.name)