rivers = {"nile": "egypt", "long river": "china", "yellow river": "china"}

for key, value in rivers.items():
    print(f"the {key.title()} runs through {value.title()}")

for key in rivers.keys():
    print(f"the river is {key.title()}")

for value in rivers.keys():
    print(f"the country is {value.title()}")
