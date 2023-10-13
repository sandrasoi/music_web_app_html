from lib.album import Album

"""
Album constructs with an id, title and release_year and artist_id
"""
def test_album_constructs():
    album = Album(1, "Test Title", 1000, 2)
    assert album.id == 1
    assert album.title == "Test Title"
    assert album.release_year == 1000
    assert album.artist_id == 2

"""
Format object nicely
"""
def test_format_nicely():
    album = Album(1, "Test Title", "Test release year", "Test artist id")
    assert str(album) == "Album(1, Test Title, Test release year, Test artist id)"


# """
# We can compare two identical books
# And have them be equal
# """
def test_books_are_equal():
    album1 = Album(1, "Test Title", "Test release year", "Test artist id")
    album2 = Album(1, "Test Title", "Test release year", "Test artist id")
    assert album1 == album2
    # Try commenting out the `__eq__` method in lib/book.py
    # And see what happens when you run this test again.

def test_nice_format():
    album1 = Album(1, "Test Title", "Test release year", "Test artist id")
    assert album1.nice_format() == "Title: Test Title\nReleased: Test release year"