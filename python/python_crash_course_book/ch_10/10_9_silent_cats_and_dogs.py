from pathlib import Path

def text_reader(file_name):
    path = Path(file_name)

    try:
        lines = path.read_text()

    except FileNotFoundError:
        pass

    else:
        print(f"{file_name} contains the following names: ")
        print(lines)

file_names_lst = ['cats.txt', 'dogs.txt', 'dragons.txt']

for i in file_names_lst:
    text_reader(i)


