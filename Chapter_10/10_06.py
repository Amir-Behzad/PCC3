try:
    first_number = int(input("Please type the first number: "))
    second_number = int(input("Please type the second number: "))
    sum = first_number + second_number
    print(
        f"\n{first_number} + {second_number} =",
        sum,
        "\n"
    )

except ValueError:
    print("Please type a proper number")