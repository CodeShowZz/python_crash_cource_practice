def make_album(artist_title, artist_name, number_of_song=None):
    album = {"title": artist_title, "name": artist_name}
    if number_of_song:
        album["number_of_song"] = number_of_song
    return album


while True:
    artist_title = input("please enter a artist title,enter quit to exit: ")
    if artist_title == "quit":
        break
    artist_name = input("please enter a artist name,enter quit to exit: ")
    if artist_name == "quit":
        break
    print("your input album info is")
    print(make_album(artist_title=artist_title, artist_name=artist_name))
