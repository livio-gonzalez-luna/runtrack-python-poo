# Créer une fonction qui prend en paramètre une chaine de caractère. 
# Écrire une fonction qui permet de retourner sa longueur, sans utiliser de fonction système . Attention, vous
# ne devez utiliser ni while, ni for, ni foreach

def string_length(s):
    try:
        s[0]
        return 1 + string_length(s[1:])
    except IndexError:
        return 0

str = input("Enter a string: ")
print("Length of the string is", string_length(str))
