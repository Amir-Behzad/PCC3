from pathlib import Path
import json

path = Path('favorite_numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print("Numbers:", numbers)