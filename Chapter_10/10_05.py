from pathlib import Path

path = Path("guest_book.txt")

prompt = "Write 'quit' to exit.\nName: "
names = ""
while True:
    message = input(prompt)
    if message == 'quit':
        break
    names += f"{message}\n"

path.write_text(names)