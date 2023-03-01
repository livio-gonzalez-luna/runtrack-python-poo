class CompteBancaire:
    # Constructor #
    def __init__(self, numero, nom, prenom, solde):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = False

    # Methods #
    def afficher(self):
        print(f"\nNumero de compte: {self.__numero}")
        print(f"Nom: {self.__nom}")
        print(f"Prenom: {self.__prenom}")
        print(f"Solde: {self.__solde}")

    def afficherSolde(self):
        print(f"\nSolde: {self.__solde}")

    def versement(self, montant):
        self.__solde += montant
        print(f"\nVersement de {montant} effectué. Nouveau solde: {self.__solde}")

    def retrait(self, montant):
        if self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant} effectué. Nouveau solde: {self.__solde}")
        else:
            if self.__solde - montant >= 0:
                self.__solde -= montant
                print(f"Retrait de {montant} effectué. Nouveau solde: {self.__solde}")
            else:
                print("Solde insuffisant")

    def agios(self):
        if self.__solde < 0:
            self.__solde -= 10
            print(f"Agios de 10€ appliqués. Nouveau solde: {self.__solde}")

    def virement(self, compte, montant):
        if self.__solde - montant >= 0:
            self.__solde -= montant
            compte.__solde += montant
            print(f"Virement de {montant}€ effectué. Nouveau solde: {self.__solde}")
        else:
            print("Solde insuffisant")

# Test #
compte1 = CompteBancaire(1, "Mallyday", "Johnny", 1000)
compte1.afficher()
compte1.versement(500)
compte1.retrait(1000)
compte1.afficher()

compte2 = CompteBancaire(2, "Mallyday", "Laeticia", -100)
compte2.afficher()
compte2.agios()
compte2.afficher()

compte1.virement(compte2, 1000)
compte1.afficher()
compte2.afficher()

