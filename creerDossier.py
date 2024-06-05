import os

chemin = r"D:\Projects\CoursPython";

#############################################################################
### Créer un dossier
#############################################################################


# Ici je pourrais aussi créer des sous dossiers en ajoutant simplement 
# des arguments à la fonction .join(chemin, "mondossier", "monsousdossier", etc.)
dossier = os.path.join(chemin, "mondossier"); 

# Cette condition est là pour vérifier si le dossier qu'on essaie de créer 
# existe déjà, la fonction ".makedirs()" nous renverra une erreur si on essaie
# de créer à nouveau le dossier alors qu'il est existant
# NOTE Toutefois, on peut faire autrement : os.makedirs(dossier, exist_ok=True);
# cela permettra de ne pas mettre la condition et gagner quelques lignes

# os.makedirs(dossier) sert à créer un dossier

if not os.path.exists(dossier):
    os.makedirs(dossier);
else:
    print("Dossier déjà existant");


#############################################################################
### supprimer un dossier
#############################################################################

# La structure conditionnelle est ici obligatoire, si le fichier que l'on 
# tente de supprimer n'existe pas, on aura une erreur et il n'y a pas 
# d'argument supplémentaire pour la fonction ".removedirs()"

if os.path.exists(dossier):
    os.removedirs(dossier);
else:
    print("Dossier inexistant");