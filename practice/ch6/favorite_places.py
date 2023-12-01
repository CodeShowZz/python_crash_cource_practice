favorite_places = {
    "tom": ["shenzhen", "hunan"],
    "jack": ["xiamen"],
    "mary": ["changsha", "hangzhou", "shanghai"],
}

for name, places in favorite_places.items():
    print(f"{name}'sfavorite place is ")
    for place in places:
        print(f" {place}")
