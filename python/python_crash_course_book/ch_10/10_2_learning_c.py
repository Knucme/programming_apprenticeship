from pathlib import Path

path = Path('10_learning_python.txt')
contents = path.read_text().splitlines()

lines = contents

for line in lines:
    print(line.replace("Python", "C"))


