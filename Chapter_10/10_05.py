from pathlib import Path

path = Path("guest_book.txt")

prompt = "Write 'quit' to exit.\nName: "
message = ""
while message != 'quit':
    name = message
    message = input(prompt)

path.write_text(name)