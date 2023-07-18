while True:
  print('Type two numbers to get the sum of them.')
  print("Type 'q' to exint.")

  first_number = input("First number: ")
  if first_number == "q":
     print('Exiting...')
     break
  second_number = input("Second number: ")
  if second_number == 'q':
     print('Exiting...')
     break
  
  try:
      sum = int(first_number) + int(second_number)
      print(
          f"\n{first_number} + {second_number} =",
          sum,
          "\n"
      )

  except ValueError:
      print("Please type valid numbers.\n")