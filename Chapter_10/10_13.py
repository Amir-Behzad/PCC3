from pathlib import Path
import json

user = {}
user['name'] = input("what is your name? ")
user['gender'] = input('Type "f" for female, or "m" for male: ')
path = Path('users.json')
contents = json.dumps(user)
path.write_text(contents)


print(
  f"We'll remember you when you come back, {user['name']}."
)
