import datetime

class Personne:
    def __init__(self, annee_naissance, nom, prenom):
        self.annee_naissance = annee_naissance
        self.nom = nom
        self.prenom = prenom
    def age(self):
        annee_actuelle = datetime.datetime.now().year
        return annee_actuelle - self.annee_naissance
    def etat_civil(self):
        return self.prenom + " " + self.nom
    def data(self):
        return {"annee_de_naissance":self.annee_naissance, "nom":self.nom, "prenom":self.prenom}

personne = Personne(1966, "Dupont", "Jean")

print("Personne(data).data :", personne.data())
print("Personne(data).etat_civil() :", personne.etat_civil())
print("Personne(data).age() :", personne.age())