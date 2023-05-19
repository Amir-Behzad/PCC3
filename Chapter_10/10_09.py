from pathlib import Path

print()

try:
  cats_path = Path('./cat.txt')
  cats = cats_path.read_text().splitlines()

  for cat in cats:
      print("Cat's name:", cat)
  
except FileNotFoundError:
  pass
  
print()
  
try:
  dogs_path = Path('./dog.txt')
  dogs = dogs_path.read_text().splitlines()

  for dog in dogs:
      print("Dog's name:", dog)

except FileNotFoundError:
  pass  
print()