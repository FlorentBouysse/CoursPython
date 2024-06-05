from pathlib import Path

# Ici on récupère un chemin vers le dossier utilisateur
home = Path.home();
print(home);

# Ici on récupère le chemin absolut jusqu'au fichier dans lequel on se trouve
cwd = Path.cwd();
print(cwd);

# Concaténer des chemins de deux manières :
new_way = home / "Documents" / "main.py";
print(new_way);
home.joinpath("Documents", "main.py");

# Il est possible de récupérer le suffix d'un fichier de deux manières :
suffix = (home / "Documents / main.py").suffix
print(suffix);
suffix2 = home.joinpath("Documents", "main.py").suffix;