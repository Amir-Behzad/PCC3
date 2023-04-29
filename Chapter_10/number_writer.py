from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]
names = ['Amir', 'James', 'Lana', 'John']
path = Path('numbers.json')
contents = json.dumps(numbers + names)
path.write_text(contents)