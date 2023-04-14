
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

# lines = contents.splitlines()
print("\nLines:", "\n")
for line in contents.splitlines():
    print(line)
print()