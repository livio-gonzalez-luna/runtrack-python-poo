# Écrire un programme qui demande à l’utilisateur de fournir une première chaîne de caractères, puis une seconde. 
# Le programme affiche 1 si les 2 chaines sont identiques ou 0 si les chaînes ne sont pas identiques. 
# Les chaînes ne sont constituées que de lettres minuscules. 
# La deuxième chaîne de caractères peut contenir un ou plusieurs ‘ * ‘.
# Chaque ‘ * ‘ peut remplacer 0 ou plusieurs caractères. 
# Par exemple, si la chaîne 1 est “laplateforme” et la chaine 2 “lap*”, le programme affiche 1 car l’ ‘ * ‘ remplace ‘ lateforme ‘. 
# Si la chaîne 1 est “laplateforme” et la chaîne 2 “l*a*pla*te*form***e” le programme renvoie 1 car les ‘ * ‘ ne remplace rien.


def compareStrings(string1, string2):
    # Recursive function to compare two strings #
    if len(string1) == 0 and len(string2) == 0:
        return True
    # If the first string is empty, the second string must be empty or contain only '*' #
    elif len(string2) == 0:
        return False
    # If the first character of the second string is '*', the first string can be empty or the first character of the first string can be the same as the first character of the second string #
    elif string2[0] == '*':
        return compareStrings(string1, string2[1:]) or (len(string1) > 0 and compareStrings(string1[1:], string2))
    # If the first character of the second string is not '*', the first string must not be empty and the first character of the first string must be the same as the first character of the second string #
    else:
        return len(string1) > 0 and string1[0] == string2[0] and compareStrings(string1[1:], string2[1:])

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# If the two strings are identical, print 1 #
if compareStrings(string1, string2):
    print("1")
# If the two strings are not identical, print 0 #
else:
    print("0")
