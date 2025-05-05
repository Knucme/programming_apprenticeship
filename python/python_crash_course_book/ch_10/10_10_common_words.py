from pathlib import Path
from re import L

def word_count(file_name):
    path = Path(file_name)

    try:
        lines = path.read_text().splitlines()
    except FileNotFoundError:
        pass
    else:
        count = 0
        for line in lines:
            count += line.count("The ")
        print(f"Final count is #{count}")

def read_book_lst(book_lst):
    path = Path(book_lst)
    
    try:
        lines = path.read_text().splitlines()

    except FileNotFoundError:
        pass
    
    else:
        for line in lines:
            word_count(line)

read_book_lst("books.txt")
