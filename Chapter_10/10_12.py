from pathlib import Path
import json

path = Path('numbers.json')

prompt = "Type 'q' to exit\n"
prompt += "Your favorite number: "

content = path.read_text()
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
