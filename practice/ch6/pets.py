dog = {"kind": "dog", "owner": "jack"}
cat = {"kind": "cat", "owner": "tom"}
pets = [dog, cat]
for pet in pets:
    print(
        f"the animal's kind is {pet['kind'].title()} and the owner is {pet['owner'].title()}"
    )
