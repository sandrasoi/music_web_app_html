from lib.artist_repository import ArtistRepository
from lib.artist import Artist

"""artist repository:
Given a list of artists
Show me all the artists names

repository.all() => Pixies, Abba"""
def test_list_all_artists(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = ArtistRepository(db_connection)
    assert repository.all() == [Artist(1, 'Pixies', 'Rock'), Artist(2, 'ABBA', 'Pop'), Artist(3, 'Taylor Swift', 'Pop'), Artist(4, 'Nina Simone', 'Jazz')]

# """Given an artist is added to a list
# Show me the updated list of artist names with the added artist"""

def test_list_all_artists(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = ArtistRepository(db_connection)
    artist = Artist(None, "Doja Cat", "Pop")
    repository.add(artist)
    assert repository.all() == [Artist(1, 'Pixies', 'Rock'), Artist(2, 'ABBA', 'Pop'), Artist(3, 'Taylor Swift', 'Pop'), Artist(4, 'Nina Simone', 'Jazz'), Artist(5, 'Doja Cat', 'Pop')]
    

def test_find_one_artist(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = ArtistRepository(db_connection)
    artist_one = repository.find(1)
    assert artist_one == Artist(1, 'Pixies', 'Rock')