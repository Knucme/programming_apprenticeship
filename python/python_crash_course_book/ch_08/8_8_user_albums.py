def make_album(artist_name, album_title, num_songs=None):
    album = {
            "name": artist_name,
            "title": album_title,
            }
    if num_songs != None:
        album["number of songs"] = num_songs

    return album

while True:
    print("Welcome to the Album generator\nTo exit enter esc")

    artist_name = input("Enter artist name: ")
    if artist_name.lower() == "esc":
        break
    album_name = input("Enter album name: ")
    if album_name.lower() == "esc":
        break
    album = make_album(artist_name, album_name)
    print(f"You just made the following album: \n{album}")
