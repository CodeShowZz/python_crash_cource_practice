map = {}
while True:
    place = input(
        "If you could visit one place in the world, where would you go,enter quit to exit?"
    )
    if place == "quit":
        break
    if place not in map:
        map[place] = 1
    else:
        map[place] = map[place] + 1

for place, count in map.items():
    print(f"the {place} poll count is {count}")
