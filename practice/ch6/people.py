james = {
    "first_name": "james",
    "last_name": "harden",
    "age": 32,
    "city": "Los Angeles",
}

tom = {
    "first_name": "tom",
    "last_name": "mick",
    "age": 26,
    "city": "Golden",
}

lake = {
    "first_name": "lake",
    "last_name": "larry",
    "age": 16,
    "city": "Houston",
}

people = [james, tom, lake]

for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person["age"]
    city = person["city"].title()

    print(f"{name}, of {city}, is {age} years old.")
