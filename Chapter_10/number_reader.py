from pathlib import Path
import json

path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(
    'Numbers:',
    numbers,
    
    '\nType of "Numbers":',
    type(numbers)

)