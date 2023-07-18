from pathlib import Path
import json

path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(
    'Numbers:',
    numbers,
    
    '\nType of "Numbers":',
    type(numbers),
    
    '\nType of "contents":',
    type(contents)

)

print()

for item in numbers:
    print(item)
    
print()