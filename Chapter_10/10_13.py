from pathlib import Path
import json

user = {}
user['name'] = input("what is your name? ")
user['gender'] = input('Type "f" for female, or "m" for male: ')
path = Path('users.json')
contents = json.dumps(user)
path.write_text(contents)

contents = path.read_text()
user_dictionary = json.loads(contents)

for key, value in user.items():
  print(f"User's {key.title()}: {value.title()}")