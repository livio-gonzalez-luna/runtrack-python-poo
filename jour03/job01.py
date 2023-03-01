# Classe Ville #
class City:
    # Constructor #
    def __init__(self, name, population):
        self.__name = name
        self.__population = population

    # Getters #
    def get_name(self):
        return self.__name
    
    def get_population(self):
        return self.__population

    # Methods #
    # Add 1 to the population #
    def add_population(self):
        self.__population += 1

# Classe Personne #
class Person:
    def __init__(self, name, age, city):
        self.__name = name
        self.__age = age
        self.__city = city

    def add_population(self):
        self.__city.add_population()

    
# Create City objects
paris = City("Paris", 1000000)
marseille = City("Marseille", 861635)

# Print the population of each city
print(f"Population of {paris.get_name()}: {paris.get_population()}")
print(f"Population of {marseille.get_name()}: {marseille.get_population()}")

# Create Person objects
john = Person("John", 45, paris)
myrtille = Person("Myrtille", 4, paris)
chloe = Person("Chloé", 18, marseille)

# Add new people to the cities
john.add_population()
myrtille.add_population()
chloe.add_population()

# Print the new population of each city
print(f"Population of {paris.get_name()}: {paris.get_population()}")
print(f"Population of {marseille.get_name()}: {marseille.get_population()}")
