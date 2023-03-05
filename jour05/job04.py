# Écrire une fonction récursive permettant de retourner le plus grand chiffre d’une liste.

def maxList(list):
    # Recursive function to return the largest number in a list #
    if len(list) == 1:
        return list[0]
    else:
        # The largest number in a list is the largest number in the list without the first element #
        return max(list[0], maxList(list[1:]))
    
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(maxList(list))


