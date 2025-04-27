def make_album(artist_name, album_title, num_songs=None):
    album = {
            "name": artist_name,
            "title": album_title,
            }
    if num_songs != None:
        album["number of songs"] = num_songs

    return album

thriller = make_album("Michael Jackson", "Thriller")
the_dark_side_of_the_moon = make_album("Pink Floyd", "The Dark Side of the Moon", 10)
rumours = make_album("Fleetwood Mac","Rumours")

print(thriller)
print(the_dark_side_of_the_moon)
print(rumours)

