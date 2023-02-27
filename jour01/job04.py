class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def SePresenter(self):
        return f"Je suis {self.name} {self.surname}."

# Creating instances of the Person class
person1 = Person("John", "Doe")
person2 = Person("Jean", "Dupont")

# Calling the SePresenter() method for each instance
print(person1.SePresenter())
print(person2.SePresenter())
