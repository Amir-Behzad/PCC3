from pathlib import Path

path = Path('learning_python.txt')

content = path.read_text()

print("The content of the file:",
  f"\n{content}")


# lines = content.splitlines()
print("\nLines:")
for line in content.splitlines():
  print(line)