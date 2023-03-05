# Créer un programme demandant à l’utilisateur de renseigner un nombre entier.

# Votre programme devra calculer la factorielle de ce nombre, sans utiliser de fonction autre que les vôtres. 

# Attention, vous ne devez utiliser ni while, ni for, ni foreach ni ... boucle. Seulement de la récursivité



def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter an integer: "))
print("Factorial of", num, "is", factorial(num))
