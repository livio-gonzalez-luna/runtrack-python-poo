# Créer un programme demandant à l’utilisateur de renseigner un nombre entier. 

# Votre programme devra calculer x^n, où n est le nombre fourni par l’utilisateur, sans utiliser de fonction autre que les vôtres. 

# Attention, vous ne devez utiliser ni while, ni for, ni foreach ni ... boucle. Seulement de la récursivité.



def power(x, n):
    # Recursive function to calculate x^n #
    if n == 0:
        return 1
    # If n is even, x^n = (x^(n/2))^2 #
    elif n % 2 == 0:
        return power(x, n//2) ** 2
    # If n is odd, x^n = x * x^(n-1) #
    else:
        return x * power(x, n-1)


x = int(input("Enter a number: "))
n = int(input("Enter a non-negative integer: "))
print(x, "^", n, "=", power(x, n))


