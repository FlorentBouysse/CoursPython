from pathlib import Path

p = Path.cwd() / "ManipulationFichier" / "pathlib" / "img.png";

# p.touch();

p = p.parent / (p.stem + "-lowres" + p.suffix)

# p.touch();
# print(p);

