pizzas = ["pizza1", "pizza2", "pizza3"]
friend_pizzas = pizzas[:]

pizzas.append("pizza4")
friend_pizzas.append("pizza5")

print("My favorite pizzas are")
for pizza in pizzas:
    print(pizza)

print("My friends'favorite pizzas are")
for pizza in friend_pizzas:
    print(pizza)
