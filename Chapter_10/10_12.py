from pathlib import Path
import json


prompt = "Type 'q' to exit\n"
prompt += "Your favorite number: "
numbers = []

try:
    path = Path('numbers.json')
    content = path.read_text()
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    numbers = json.loads(content)
    numbers = list(numbers)
    

while True:
    number = input(prompt)
    if number == "q":
        break
    else:
        try:
            number = int(number)
            if number not in numbers:
                numbers.append(number)
            else:
                print(f"{number} was already added.")
        except:
            print("wrong input.")

content = json.dumps(numbers)
path.write_text(content)

print('\nNumbers: ')
for number in numbers:
    print(number)
    
print()
