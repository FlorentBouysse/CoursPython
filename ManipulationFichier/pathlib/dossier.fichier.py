# Créer / Supprimer un fichier et un dossier avec Pathlib
from pathlib import Path
import shutil

#############################################################
## DOSSIER
#############################################################

# .cwd() est le chemin absolu jusqu'au dossier actuel
p = Path.cwd();

p = p / "ManipulationFichier" / "pathlib" / "DossierTest";

print(p);
# L'argument "exist_ok=True" est ici pour éviter une erreur
# si jamais le dossier existe déjà
p.mkdir(exist_ok=True);

p = p / "1" / "2" / "3";

# Le paramètre "parents=True" permet la création de plusieurs
# dossiers les uns dans les autres sinon cela retournera un erreur
p.mkdir(exist_ok=True, parents=True);



#############################################################
## FICHIER
#############################################################

p = p / "fichierTest.txt";

# Créer le fichier
p.touch();

# Supprimer le fichier
p.unlink();



#############################################################
## Supprimer un dossier
#############################################################

# Ici, pour rappel, nous sommes au niveau du "fichierTest.txt" donc
# pour remonter d'un cran, nous utilisons ".parent"
p = p.parent;

# Ici nous supprimons un dossier vide
p.rmdir();

# Ici nous remontons de trois crans pour supprimer le dossier "DossierTest"
p = p.parent.parent.parent;

# Pour supprimer un dossier qui n'est pas vide, il faut importer "shutil"
# et faire la commande en dessous
shutil.rmtree(p);
