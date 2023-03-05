# Créer une fonction qui prend en paramètre une chaine de caractère. 

# Écrire une fonction qui permet de retourner sa longueur, sans utiliser de fonction système . Attention, vous ne devez utiliser ni while, ni for, ni foreach

def string_length(str):
    # Recursive function to return the length of a string #
    try:
        # The length of a string is the length of the string without the first character #
        str[0]
        return 1 + string_length(str[1:])
    # If the string is empty, return 0 #
    except IndexError:
        return 0

str = input("Enter a chain of characters: ")
print("Length of the chain of charchters is", string_length(str))
