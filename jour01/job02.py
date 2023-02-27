# Define class called "Operation" #
class Operation:

    # Define constructor #
    # Define the arguments, number1 & number2 with default value 0 #
    def __init__(self, number1 = 0, number2 = 0):
        # Create two instance variables (number1 & number2) #
        # Assign them the values of the arguments passed in the the constructor #
        self.number1 = number1
        self.number2 = number2


# Create instance from "Operation" class #
op = Operation(12,3)

# Print the values of the instance variables #
print("Le nombre1 est", op.number1)
print("Le nombre2 est", op.number2)
