import json

chemin = r"D:\Projects\CoursPython\fichier.json";

# Ici on écrit du json grâce à ".dump()", dans le fichier
# Les guillemets resteront
with open(chemin, 'w') as f:
    json.dump("Bonjour", f);

# On créer et écrit une liste que l'on affiche sur plusieurs
# lignes avec une indentation de 4
with open(chemin, 'w') as f:
    json.dump(list(range(10)), f, indent=4);

# Ici on lit de fichier json avec la fonction ".load()"
with open(chemin, 'r') as f:
    liste = json.load(f);
    print(liste);

# Ici on ajoute des données dans une liste
# Il n'est pas possible de faire autrement, nous devons lire
# puis réécrire le fichier
with open(chemin, "r") as f:
    datas = json.load(f);
    
datas.append(4);

with open(chemin, "w") as f:
    json.dump(datas, f, indent=4);


###################################################################################
### ERREUR COURANTE
###################################################################################

# Il n'est pas possible de lire un fichier vide, cela retournera une erreur
# donc mettre "" ou [] dans le fichier

# Si on écrit par exemple "Pèche" cela écrira "P\u00e8che", cela ne posera 
# aucun problème pour la lecture du fichier mais c'est moins lisible si 
# on va directement dedans donc rajouter le param "ensure_ascii=False"
with open(chemin, "w") as f:
    json.dump("Pèche", f, ensure_ascii=False);

with open(chemin, "r") as f:
    liste = json.load(f);
    print(liste);