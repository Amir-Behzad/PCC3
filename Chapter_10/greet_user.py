from pathlib import Path
import json

path = Path('user_names.json')
contents = path.read_text()
userName = json.loads(contents)

print(
    f"Welcome back, {userName}"
)