from pathlib import Path
import json

number = input("Your favourite number: ")

path = Path('favorite_numbers.json')
contents = json.dumps(number)
path.write_text(contents)
