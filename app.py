from flask import Flask
from flask import Flask, render_template
from pymongo import MongoClient

cline = MongoClient()
db = clinet.Playlister
playlists = db.playlists



app = Flask(__name__)



@app.route('/')
def index():
    """Return homepage."""
    # change the original return statement you wrote to the one below
    return render_template('home.html', msg='Flask is Cool!!')


app = Flask(__name__)


# playlists = [
#     { 'title': 'Cat Videos', 'description': 'Cats acting weird' },
#     { 'title': '80\'s Music', 'description': 'Don\'t stop believing!' }
# ]

# playlists = [
#   { 'title': 'Great Playlist' },
#   { 'title': 'Next Playlist' }
# ]



@app.route('/')
def playlists_index():
    """Show all playlists."""
    # Update this line
    return render_template('playlists_index.html', playlists=playlists.find())



if __name__ == '__main__':
    app.run(debug=True)
