from flask import Flask, render_template
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