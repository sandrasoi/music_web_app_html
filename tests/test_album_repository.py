from lib.album_repository import AlbumRepository
from lib.album import Album

"""When I call all
I get all the albums in the albums table"""

def test_list_albums(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    assert repository.all() == [Album(1, 'Doolittle', 1989, 1), Album(2, 'Surfer Rosa', 1988, 1)]

"""
When we call BookRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    repository.create(Album(3, 'Scarlet', 2023, 3))
    assert repository.all() == [Album(1, 'Doolittle', 1989, 1), Album(2, 'Surfer Rosa', 1988, 1), Album(3, 'Scarlet', 2023, 3)]





"""
When we call AlbumRepository#find
We get a single Book object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)

    book = repository.find(2)
    assert book == Album(2, "Surfer Rosa", 1988, "Pixies")

# """
# When we call BookRepository#create
# We get a new record in the database.
# """
# def test_create_record(db_connection):
#     db_connection.seed("seeds/book_store.sql")
#     repository = BookRepository(db_connection)

#     repository.create(Book(None, "The Great Gatsby", "F. Scott Fitzgerald"))

#     result = repository.all()
#     assert result == [
#         Book(1, "Invisible Cities", "Italo Calvino"),
#         Book(2, "The Man Who Was Thursday", "GK Chesterton"),
#         Book(3, "Bluets", "Maggie Nelson"),
#         Book(4, "No Place on Earth", "Christa Wolf"),
#         Book(5, "Nevada", "Imogen Binnie"),
#         Book(6, "The Great Gatsby", "F. Scott Fitzgerald"),
#     ]

# """
# When we call BookRepository#delete
# We remove a record from the database.
# """
# def test_delete_record(db_connection):
#     db_connection.seed("seeds/book_store.sql")
#     repository = BookRepository(db_connection)
#     repository.delete(3) # Apologies to Maggie Nelson fans

#     result = repository.all()
#     assert result == [
#         Book(1, "Invisible Cities", "Italo Calvino"),
#         Book(2, "The Man Who Was Thursday", "GK Chesterton"),
#         Book(4, "No Place on Earth", "Christa Wolf"),
#         Book(5, "Nevada", "Imogen Binnie"),
#     ]
