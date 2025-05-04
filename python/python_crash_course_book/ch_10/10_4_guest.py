from pathlib import Path

path = Path('guest.txt')

usr_name = input("Enter your name: ")

file_content = path.write_text(usr_name)
