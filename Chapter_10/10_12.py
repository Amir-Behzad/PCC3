from pathlib import Path
import json

path = Path('users.json')
numbers_list = [2, 5, 1, 6, 3]
content = json.dumps(numbers_list)
path.write_text(content)

contents = path.read_text()
numbers = json.loads(contents)
print('\nNumbers: ')
for number in numbers:
    print(number)
    
print()

