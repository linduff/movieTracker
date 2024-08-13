from flask import Flask, render_template, jsonify
# import tmdb
import json

app = Flask(__name__)

# popular_movies = tmdb.movie(1022789)
# print(popular_movies)

# @app.route("/")
# def main():
#     popular_movies = tmdb.popular_movies()
#     return render_template("home.html", movies = popular_movies)

@app.route("/")
def search():
    searchResults = json.load(open('testFiles/searchResults_star_wars.json'))
    return render_template("search.html", searchResults=searchResults)

# @app.route("/search/<query>")
# def search(query):
#     return render_template("search.html", results=jsonify(tmdb.search_movies(query)))

# @app.route("/movie/<movie_id>")
# def movie(movie_id):
#     return render_template("movie.html", movie=tmdb.movie(movie_id))

@app.route('/healthcheck')
def health():
    resp = jsonify(health="healthy")
    resp.status_code = 200
    return resp

if __name__ == "__main__":
    app.run()