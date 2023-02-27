class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Method to display the coordonates #
    def afficherLesPoints(self):
        print(f"({self.x}, {self.y})")

    # Method to Display X #
    def afficherX(self):
        print(f"x = {self.x}")

    # Method to Display Y #
    def afficherY(self):
        print(f"y = {self.y}")

    # Method to Change X #
    def changerX(self, newX):
        self.x = newX

    # Method to Change Y #
    def changerY(self, newY):
        self.y = newY


# Creating an instance of the Point class
point = Point(7, 8)

# Testing the methods of the Point class
point.afficherLesPoints()

point.afficherX()      
point.afficherY()      

point.changerX(89)
point.changerY(356)

point.afficherLesPoints()