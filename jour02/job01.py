class Rectangle:
    # Constructor #
    def __init__(self, length, width):
        self.__length = length # " __ " before attribute name indicates that is a private attribute #
        self.__width = width # Private attribute #

    # Getters and setters #
    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

# Create a rectangle with length 10 and width 5
rectangle = Rectangle(10, 5)

# Change the length and width of rectangle #
rectangle.set_length(20)
rectangle.set_width(10)

print("The rectangle has a length of", rectangle.get_length(), "and a width of", rectangle.get_width())
