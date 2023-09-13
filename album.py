
def make_album(artist, title, songs=None):
    album = {
        'artist': artist,
        'title': title
    }
    if songs is not None:
        album['songs'] = songs
    return album

# Creating dictionaries for Phil John's albums
album1 = make_album('Phil John', 'First Album')
album2 = make_album('Phil John', 'Second Album', songs=10)
album3 = make_album('Phil John', 'Third Album', songs=12)

# Printing the album dictionaries
print(album1)
print(album2)
print(album3)
