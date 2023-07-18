while True:
    prompt = "Type 'q' to exit. "
    print('Type two numbers to get the sum of them.')
    first_number = input(prompt + "\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input(prompt + "\nSecond number: ")
    if second_number == 'q':
        break

    try:
        sum = int(first_number) + int(second_number)

    except ValueError:
        print("Please type valid numbers.")

    else:
        print(
            f"\n{first_number} + {second_number} =",
            sum,
            "\n"
        )
        