from pathlib import Path
# import json

path = Path('number_writer.py')
contents = path.read_text()
# numbers = json.loads(contentsd)

print(
    "\nContents:",
    f"\n\n{contents}",
    '\n'
)