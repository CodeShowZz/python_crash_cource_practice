def make_album(artist_title, artist_name,number_of_song=None):
    album = {"title": artist_title, "name": artist_name}
    if(number_of_song):
        album['number_of_song'] = number_of_song
    return album

print(make_album('十一月的肖邦','周杰伦'))
print(make_album('依然范特西','周杰伦'))
print(make_album('vae','许嵩'))
print(make_album('有何不可','许嵩',50))
