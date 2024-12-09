class Livre:
    #Compteur initié
    nombre_editions = 0
    commentaires = []

    def __init__(self, auteur, titre, annee_publication):
        self.auteur = auteur
        self.titre = titre
        self.annee_publication = annee_publication
        #Incrémentation compteur
        Livre.nombre_editions += 1
        

#Méthode pour afficher les détails
def afficher_details(self):
    print(f"{self.titre}, {self.auteur}, {self.annee_publication}")

#Méthode pour afficher le nombre d'éditions
def get_nombre_editions(self):
    print(f"Le nombre d'éditions est {Livre.nombre_editions}")

#Méthode pour ajouter commentaire
def ajouter_commentaire(self, commentaire):
    Livre.commentaires.append(commentaire)

#Méthode pour afficher commentaire
def afficher_commentaire(self):
    for commentaire in Livre.commentaires:
        print(f"Commentaire: {commentaire}")
#Instances
seigneur_anneaux = Livre("J.R.R Tolkien", "Le Seigneur des Anneaux", 1956)
harry_potter = Livre("J.K. Rowling", "Harry Potter", 1997)

#Pour cette méthode j'ai utilisé cette ressource pour comprendre comment faire :https://medium.com/@DavidHofff/what-is-the-eq-method-in-python-classes-614779526843
#Mais en fait ça m"a un peu embrouillé parce que __eq__ renvoie des booléens et ici on voulait des phrases
def eq(self, other):
    if (self.titre == other.titre and
    self.auteur == other.auteur and
    self.annee_publication == other.annee_publication):
        print("Les livres sont identiques")
    else:
        print("Les livres ne sont pas identiques")

#Instances pour l'exercice APP-6
livre1 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 1954)
livre2 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 1954)

livre3 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 1956)
livre4 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 1954)

#Utilisation méthodes pour l'exercice APP-7
livre1.ajouter_commentaire("Excellent livre!")
livre2.ajouter_commentaire("J'ai adoré l'intrigue.")
Livre.afficher_commentaires()
#Ici cela me renvoie un Attribute Error je ne comprends pas pourquoi "Livre object has no attribute ajouter_commentaire"
    
#Utilisation des méthodes
afficher_details(seigneur_anneaux)
afficher_details(harry_potter)
get_nombre_editions(Livre)
eq(livre1, livre2)
eq(livre3, livre4)