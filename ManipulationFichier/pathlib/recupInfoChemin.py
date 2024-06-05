from pathlib import Path

p = Path.cwd();

new_path = p / "Documents" / "main.py";

# Pour savoir tout ce qu'il est possible de faire avec Path
# print(dir(p))

# Fonction utile avec Path
print("1. Nom du fichier + extension : ");
print(new_path.name);
print("2. Le parent du fichier : ");
print(new_path.parent);
print("3. nom du fichier : ");
print(new_path.stem);
print("4. extension : ");
print(new_path.suffix);
print("5. s'il y a plusieurs extensions : ");
print(new_path.suffixes);
print("6. Récupère les parties du chemin : ");
print(new_path.parts);
print("7. est-ce qu'il existe : ");
print(new_path.exists());
print("8. Si c'est un dossier : ");
print(new_path.is_dir());
print("9. Si c'est un fichier : ");
print(new_path.is_file());