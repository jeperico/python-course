from pathlib import Path

path = Path("placeholder")
if not path.exists():
    path.mkdir()

# print(path.exists())

for file in Path().glob('*.py'):
    print(file)

path.rmdir()
