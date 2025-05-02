from pathlib import Path

path = Path('10_learning_python.txt')
contents = path.read_text()

lines = contents.splitlines()

print("Solution #1: ")

print(contents)

print("Solution #2: ")

new_lst = []
for line in lines:
    new_lst.append(line)

print(new_lst)
