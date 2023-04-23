print('Type two numbers to get the sum of them.')
first_number = input("First number: ")
second_number = input("Second number: ")

try:
    sum = int(first_number) + int(second_number)
    print(
        f"\n{first_number} + {second_number} =",
        sum,
        "\n"
    )

except ValueError:
    print("Please type valid numbers.")