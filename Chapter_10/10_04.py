from pathlib import Path

name = input("Your Name: ")

path = Path("./Chapter_10/guest.txt")

path.write_text(name)
