from pathlib import Path

path = Path('guest_book.txt')

guests = ''
while True:
    usr_name = input("Enter a name: ")
    guests += usr_name + "\n"
    path.write_text(guests)
    usr_cont = input("Continue y/n: ")
    if usr_cont == 'n':
        break
