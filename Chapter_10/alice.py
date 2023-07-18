from pathlib import Path

path = Path('alice.txt')
try:
    content = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f'{path} not found')

else:
    # Count the approximate number of words in the file:
    words = content.split()
    num_words = len(words)
    print(f"The file '{path}' has {num_words} words.")
    
