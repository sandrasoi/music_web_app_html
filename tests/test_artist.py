from lib.artist import Artist

"""
Album constructs with an id, title and release_year and artist_id
"""
def test_arist_constructs():
    artist = Artist(1, "Doja Cat", "genre")
    assert artist.id == 1
    assert artist.name == "Doja Cat"
    assert artist.genre == "genre"

# """
# We can compare two identical books
# And have them be equal
# """
def test_books_are_equal():
    artist1 = Artist(1, "Test name", "Test genre")
    artist2 = Artist(1, "Test name", "Test genre")
    assert artist1 == artist2
    # Try commenting out the `__eq__` method in lib/book.py
    # And see what happens when you run this test again.


"""
Format object nicely
"""
def test_format_nicely():
    artist = Artist(1, "Test name", "Test genre")
    assert str(artist) == "Artist(1, Test name, Test genre)"



