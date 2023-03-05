# Créer un programme demandant à l’utilisateur de renseigner un nombre entier.

# Votre programme devra calculer la factorielle de ce nombre, sans utiliser de fonction autre que les vôtres. 

# Attention, vous ne devez utiliser ni while, ni for, ni foreach ni ... boucle. Seulement de la récursivité



def factorial(n):
    # Recursive function to calculate the factorial of a number #
    if n == 1:
        return 1
    # The factorial of a number is the product of the number and the factorial of the number minus 1 #  
    else:
        return n * factorial(n-1)

num = int(input("Enter an integer: "))
print("Factorial of", num, "is", factorial(num))
