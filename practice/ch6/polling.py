favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

names = ["tom", "jack", "jen", "phil"]

for name in names:
    if favorite_languages.get(name, ""):
        print(f"{name},thanking you for responding.")
    else:
        print(f"{name}, inviting them to take the poll")
