from pathlib import Path

p = Path.cwd() / "ManipulationFichier" / "pathlib" / "test.txt";

p.touch();

# Pour écrire dans le fichier
p.write_text("Yo les gars !");

# Pour lire le fichier
print(p.read_text());