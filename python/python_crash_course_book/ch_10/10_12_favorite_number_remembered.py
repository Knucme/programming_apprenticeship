from pathlib import Path
import json

path = Path('favorite_number.json')
contents = path.read_text()

msg = json.loads(contents)

print(msg)
