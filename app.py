import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)


@app.route('/albums', methods=['POST'])
def post_albums():
    if 'title' not in request.form or 'release_year' not in request.form or 'artist_id' not in request.form:
        return "You need to submit a title, release year and artist id", 400
    connection = get_flask_database_connection(app)
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']
    repository = AlbumRepository(connection)
    repository.create(Album(None, title, release_year, artist_id))
    return '', 200

# @app.route('/albums', methods=['GET'])
# def get_albums():
#     connection = get_flask_database_connection(app) #what is happening here???
#     repository = AlbumRepository(connection)
#     return "\n".join([
#             str(album) for album in repository.all()
#         ])

# @app.route('/artists', methods = ['GET'])
# def get_artists():
#     connection = get_flask_database_connection(app)
#     repository = ArtistRepository(connection)
#     return repository.all()

@app.route('/artists', methods = ['POST'])
def post_artists():
    connection = get_flask_database_connection(app)
    name = request.form['name']
    genre = request.form['genre']
    artist = Artist(None, name, genre)
    ArtistRepository(connection).add(artist)
    return ""


# @app.route("/albums", methods = ['GET'])
# def get_albums():
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     #album_list = [album.nice_format() for album in repository.all()]
#     #album_list = '\n'.join([str(album) for album in repository.all()])
#     #list_albums = repository.all()
#     albums = repository.all()
#     return render_template('albums/index.html', albums = albums)

@app.route('/albums/practise', methods=['GET'])
def get_practise():
    return render_template('albums/practise.html')

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app) #what is happening here???
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template("albums/index.html", albums = albums)

#get single album using arguments
# @app.route('/albums/one_album', methods = ['GET'])
# def get_one_album():
#     connection = get_flask_database_connection(app)
#     album = AlbumRepository(connection)
#     album_id = request.args['album_id']
#     one_album = album.find(album_id)
#     return render_template('albums/one_album.html', album_title = one_album.title, release_year = one_album.release_year, artist = one_album.artist_id)

@app.route('/albums/<id>', methods = ['GET'])
def get_one_album(id):
    connection = get_flask_database_connection(app)
    album = AlbumRepository(connection)
    one_album = album.find(id)
    return render_template('albums/one_album.html', album_title = one_album.title, release_year = one_album.release_year, artist = one_album.artist_id)

@app.route('/artists/<id>', methods = ['GET'])
def get_one_artist(id):
    connection = get_flask_database_connection(app)
    artist = ArtistRepository(connection)
    one_artist = artist.find(id)
    return render_template('artists/one_artist.html', artist_name = one_artist.name, artist_genre = one_artist.genre)

@app.route('/artists', methods = ['GET'])
def get_all_artists():
    connection = get_flask_database_connection(app)
    artist = ArtistRepository(connection)
    all_artists = artist.all()
    return render_template('artists/index.html', all_artists = all_artists)



# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))


