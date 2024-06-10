from pathlib import Path

# Ceci retournera un objet à itérer
p = Path().iterdir();

print(p);

# Ceci affiche tous les dossiers et fichiers du dossier où nous nous trouvons
for f in p:
    print(f);

# # Ceci affiche seulement les dossiers avec ".is_dir()"
for f in p:
    if f.is_dir():
        print(f);

# Ceci affiche seulement les fichiers avec ".is_file()"
for f in p:
    if f.is_file():
        print(f);


#############################################################
## GLOB
#############################################################

p = Path.cwd();

p.glob("*.py");

# Retournera les chemins de tout les fichiers py, si on ne veut que le nom,
# on peut mettre dans le print "i.name"
# ".glob" ne cherchera que dans le dossier courant tendit que ".rglob" ira 
# dans les sous-dossiers
for i in p.glob("*.py"):
    print(i);
    print(i.name);

print("#######################");

for i in p.rglob("*.py"):
    print(i);
    print(i.name);