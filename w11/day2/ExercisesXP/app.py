# Exercises XP
# Exercise 2
import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('cv_index.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
