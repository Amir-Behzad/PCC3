pizzas = [
    'Veggie',
    'Pepperoni ',
    'Meat',
    'Margherita',
    'BBQ Chicken',
    'Chicago',
]

friend_pizzas = pizzas[:]

pizzas.append('Chicken Mushroom')
friend_pizzas.append('Beef Mushroom')


print()
print(
    "The lists are the same:",
    pizzas == friend_pizzas
)
print()

print("My pizzas:")
for pizza in pizzas:
    print(pizza, end=", ")

print("\n")

friends_pizzas_str = ""
for pizza in friend_pizzas:
    friends_pizzas_str += pizza + ", "

print("My friends pizzas:")
print(friends_pizzas_str.removesuffix(", ") + '.')

print("\n")
