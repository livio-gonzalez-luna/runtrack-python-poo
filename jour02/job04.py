class Student:
    # Constructor #
    def __init__(self, name, prenom, credits = 0, numEtudiant = 0):
        self.__name = name
        self.__prenom = prenom
        self.__numEtudiant = numEtudiant
        self.__credits = credits
        self.__level = self.__studentEval()

    # Getters and Setters #
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    def getPrenom(self):
        return self.__prenom
    
    def getCredits(self):
        return self.__credits
    
    # The number of credits must be a positive integer #
    def setCredits(self, credits):
        if credits > 0:
            self.__credits += credits
        else:
            print("The number of credits must be a positive integer")
    
    # Methods #
    #  Private method to evaluate the student #
    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
        
    def studentInfo(self):
        print("Nom: ", self.__name)
        print("Prénom: ", self.__prenom)
        print("Id: ", self.__numEtudiant)
        print("Niveau: ", self.__level)


# Test #
students = []

student1 = Student("John", "Doe", 90, 12)
students.append(student1)

student2 = Student("Jane", "Dwoel", 80, 13)
students.append(student2)

student3 = Student("Jack", "Dep", 70, 14)
students.append(student3)

student4 = Student("Jill", "Doe", 60, 15)
students.append(student4)

for student in students:
    student.studentInfo()
    print()