from pathlib import Path
import json

path = Path('user_names.json')
contents = path.read_text()
user = json.loads(contents)

print(
  f"\nThe previous user name: {user}!\n"
)

while True:
  userName = input("what is your name? ")
  if userName == user:
    print("You cannot use the previous user.")
  else:
    user = userName
    break

new_content = json.dumps(user)
path.write_text(new_content)

print(
  f"\nWe'll remember you when you come back, {new_content}!\n"
)
