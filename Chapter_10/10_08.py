from pathlib import Path

print()

try:
  cats_path = Path('./cats.txt')
  cats = cats_path.read_text().splitlines()

  for cat in cats:
      print("Cat's name:", cat)
  
except FileNotFoundError:
  print('\nFile not found for cats.\n')
  
print()
  
try:
  dogs_path = Path('./dogs.txt')
  dogs = dogs_path.read_text().splitlines()

  for dog in dogs:
      print("Dog's name:", dog)

except FileNotFoundError:
  print('\nFile not found for dogs.\n')
  
print()