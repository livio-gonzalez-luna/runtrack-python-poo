# Écrire une fonction récursive qui calcule le n-ième nombre de la suite de Fibonacci.

# La suite de Fibonacci est une suite de nombres où chaque nombre est la somme des deux nombres précédents. 
# Elle commence par 0 et 1, et les premiers termes sont donc :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, etc.

# Attention, vous ne devez utiliser ni while, ni for, ni foreach,ni ... boucle. Seulement de la récursivité


def fibonacci(n):
    # Recursive function to calculate the nth number in the Fibonacci sequence #
    if n <= 1:
        return n
    else:
        # The nth number in the Fibonacci sequence is the sum of the (n-1)th and (n-2)th numbers in the sequence #
        return fibonacci(n-1) + fibonacci(n-2)

number = int(input("Enter a number: "))
print("The", number, "th number in the Fibonacci sequence is", fibonacci(number))


