from pathlib import Path

try:
  cats_path = Path('./cat.txt')
  cats = cats_path.read_text().splitlines()

  for cat in cats:
      print("Cat's name:", cat)
  
except FileNotFoundError:
  print('\nFile not found for cats.\n')
  
try:
  dogs_path = Path('./dogs.txt')
  dogs = dogs_path.read_text().splitlines()

  for dog in dogs:
      print("Dog's name:", dog)

except FileNotFoundError:
  print('\nFile not found for dogs.\n')
  