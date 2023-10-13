from lib.artist import Artist

class ArtistRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        all_artists = self._connection.execute("SELECT * FROM artists")
        all_artist_names = []
        for artist in all_artists:
            all_artist_names.append(Artist(artist['id'],artist['name'], artist['genre'] ))
        return all_artist_names
    
    def add(self, artist):
        self._connection.execute("INSERT INTO artists (name, genre) VALUES (%s, %s)", [artist.name, artist.genre])

    def find(self,id):
        one_artist = self._connection.execute("SELECT * FROM artists WHERE id=%s", [id])
        artist = Artist(one_artist[0]['id'], one_artist[0]['name'], one_artist[0]['genre'])
        return artist