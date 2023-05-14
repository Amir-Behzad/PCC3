from pathlib import Path

path = Path('alice.txt')
try:
    content = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f'{path} not found')

else:
    print(content)