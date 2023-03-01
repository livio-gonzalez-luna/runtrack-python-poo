class Tache:
    # Constructor #
    def __init__(self, titre, description, statut):
        self.titre = titre
        self.description = description
        self.statut = statut

    # Methods #
    def __str__(self):
        return f"Titre: {self.titre}, Description: {self.description}, Statut: {self.statut}"
    


class ListeDeTaches:
    # Constructor #
    def __init__(self):
        self.taches = []

    # Methods #
    # Method to add a task to the list #
    def ajouterTache(self, tache):
        self.taches.append(tache)


    # Method to remove a task from the list #
    def supprimerTache(self, tache):
        self.taches.remove(tache)

    # Method to mark a task as finished #
    def marquerCommeFinie(self, tache):
        tache.statut = "Terminée"

    # Method to display the list #
    def afficherListe(self):
        for tache in self.taches:
            print(tache)

    # Method to filter the list #
    def filterListe(self, statut):
        for tache in self.taches:
            if tache.statut == statut:
                print(tache)

tache1 = Tache("Manger", "Description 1", "A faire")
tache2 = Tache("Boire", "Description 2", "A faire")
tache3 = Tache("Dormir", "Description 3", "A faire")
tache4 = Tache("Coder", "Description 4", "A faire")

listeDeTaches = ListeDeTaches()
listeDeTaches.ajouterTache(tache1)
listeDeTaches.ajouterTache(tache2)
listeDeTaches.ajouterTache(tache3)
listeDeTaches.ajouterTache(tache4)

listeDeTaches.supprimerTache(tache2)
listeDeTaches.marquerCommeFinie(tache1)

listeDeTaches.afficherListe()


