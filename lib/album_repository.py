from lib.album import Album
# from database_connection import DatabaseConnection


class AlbumRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        all_albums = self._connection.execute("SELECT * FROM albums")
        album_objects_list = []
        for album in all_albums:
            item = Album(album['id'], album['title'], album['release_year'], album['artist_id'])
            album_objects_list.append(item)
        return album_objects_list

    def create(self, album):
        self._connection.execute("INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)", [album.title, album.release_year, album.artist_id])


    # Find a single book by its id
    def find(self, id):
        rows = self._connection.execute(
            'SELECT * from albums WHERE id = %s', [id])
        row = rows[0]
        artist = self._connection.execute('SELECT name from artists WHERE id = %s', [row['artist_id']])
        return Album(row['id'], row['title'], row['release_year'], artist[0]['name'])
    


    # # Create a new book
    # # Do you want to get its id back? Look into RETURNING id;
    # def create(self, book):
    #     self._connection.execute('INSERT INTO books (title, author_name) VALUES (%s, %s)', [
    #                              book.title, book.author_name])
    #     return None

    # # Delete a book by its id
    # def delete(self, book_id):
    #     self._connection.execute(
    #         'DELETE FROM books WHERE id = %s', [book_id])
    #     return None

# repository = AlbumRepository(DatabaseConnection)
# print(repository.all())