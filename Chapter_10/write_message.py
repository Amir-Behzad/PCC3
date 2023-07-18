from pathlib import Path

path = Path('./Chapter_10/programming.txt')
contents = "I love programming."
contents += "\nMore text."
contents += "I also love working with data.\n"
path.write_text(contents)

contents = path.read_text()
print(contents)