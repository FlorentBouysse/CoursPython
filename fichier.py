# SECTION 34 cours udemy Python


# Ici c'est un pc windows, donc il faut précéder la chaine de 
# caractère avec "r" pour qu'il n'y ait pas d'erreur
chemin = r"D:\Projects\CoursPython\text.txt";
chemin2 = r"D:\Projects\CoursPython\text2.txt";

###################################################################################
### READ FILE
###################################################################################

# Ici on ouvre le fichier en mode lecture (r) et on le ferme
# Si tu ne ferme pas, cela peux poser probleme
f = open(chemin, "r");
f.close();

# Voici une autre syntaxe pour faire la même chose qu'au dessus
# L'avantage de cette syntaxe est qu'il n'y a pas besoin de fermer

# WARNING Il se peut qu'il y ait une erreur lorsqu'on ouvre le fichier
# pour y remédier faire : with open("fichier_txt", "r", encoding='utf-8') as f:
with open(chemin, "r") as f:
    contenu = f.read();
    print(contenu);

# text2.txt contient du texte avec des retour à la ligne, Python va 
# donc l'interpréter de cette façon. Il est possible de l'interpréter 
# normalement avec "splitlines()" qui nous retournera un tableau
with open(chemin2, "r") as j:
    contenu = j.read().splitlines();
    contenu = " ".join(contenu);
    print(contenu); # même résultat qu'au dessus


###################################################################################
### WRITE FILE
###################################################################################

# Pour écrire dans un fichier, on peut utiliser "w" et la fonction ".write()" seulement
# cela supprimera le contenu du fichier cible
with open(chemin, "w") as f:
    contenu = f.write("Salut mecton !");

# "a" permet d'ajouter du contenu dans un fichier "a" == append
with open(chemin, "a") as f:
    contenu = f.write("\nAu revoir");