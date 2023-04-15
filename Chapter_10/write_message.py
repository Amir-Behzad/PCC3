from pathlib import Path

path = Path('./Chapter_10/programming.txt')
content = "I love programming."
content += "\nMore text."
path.write_text(content)

content = path.read_text()
print(content)