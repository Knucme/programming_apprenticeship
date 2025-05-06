from pathlib import Path
import json

path = Path('favorite_number.json')

usr_fav_num = input('Enter your favorite number: ')

contents = json.dumps(f"I know your favorite number! It's {usr_fav_num}")

path.write_text(contents)


