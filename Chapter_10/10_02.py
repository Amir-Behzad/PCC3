from pathlib import Path

path = Path('learning_python.txt')

contents = path.read_text()

print("\nContents:", f"\n{contents}")

modified_contents = contents.replace("Python", "C")
print("\nNew Contents:", f"\n{modified_contents}")

print("\nOriginal Contents:", f"\n{contents}")