import os 

repertoire_actuel = os.getcwd() #cherche chemin vers repertoire courant
print(repertoire_actuel) #affiche le chemin
nom_repertoire = os.path.basename(repertoire_actuel) #cherche le nom de la derniere partie du chemin
print(nom_repertoire) #affiche le nom trouvé

#j'ai commenté la partie qui suit car ça crée des bugs

#os.mkdir("nouveau_repertoire") #je cree nouveau repertoire
#os.rmdir("nouveau_repertoire") #je supprime nouveau repertoire
#pour cette partie quand je run le code ça me met Errno17 File exists mais je ne comprends pas pourquoi

liste = os.listdir(repertoire_actuel)
print(liste)