from flask import Flask, render_template
import tmdbsimple as tmdb
import os
from dotenv import load_dotenv

load_dotenv()

tmdb.API_KEY = os.getenv("API_KEY")
tmdb.REQUESTS_TIMEOUT = 5

movie = tmdb.Movies(603)
response = movie.info()
print(response.title)

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("homepage.html")

@app.route('/healthcheck')
def health():
    resp = jsonify(health="healthy")
    resp.status_code = 200
    return resp

if __name__ == "__main__":
    app.run()