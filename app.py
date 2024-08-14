from flask import Flask, render_template, jsonify, request
import tmdb
import json

app = Flask(__name__)

# popular_movies = tmdb.movie(1022789)
# print(popular_movies)

@app.route("/")
def main():
    popular_movies = tmdb.popular_movies()
    return render_template("home.html", movies = popular_movies)

@app.route("/movie/<movie_id>")
def movie(movie_id):
    return render_template("movie.html", movie=tmdb.movie(movie_id))

@app.route("/search", methods=['POST'])
def search():
    if request.method == 'POST':
        return render_template("search.html", searchResults=tmdb.search_movies(request.form['query']))
    

@app.route('/healthcheck')
def health():
    resp = jsonify(health="healthy")
    resp.status_code = 200
    return resp

if __name__ == "__main__":
    app.run()