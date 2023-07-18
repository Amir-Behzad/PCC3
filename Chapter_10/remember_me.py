from pathlib import Path
import json

userName = input("what is your name? ")
path = Path('user_names.json')
contents = json.dumps(userName)
path.write_text(contents)

print(
  f"We'll remember you when you come back, {userName}!"
)
