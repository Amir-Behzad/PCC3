from pathlib import Path

path = Path('learning_python.txt')

contents = path.read_text()

print("Contents:", contents)

modified_contents = contents.replace("Python", "C")
print("New Contents:", modified_contents)

print("Original Contents:", contents)