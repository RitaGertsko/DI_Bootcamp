from flask import Flask, render_template
from markdown import markdown
import markdown.extensions.fenced_code


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/exercises')
def exercises():
    with open('./lesson1/exercises.md', "r", encoding="utf8") as f:
        html = markdown.markdown(f.read(),  extensions=["fenced_code"])
        return html


@app.route('/lesson')
def lesson():
    with open('./lesson1/in-this-chapter.md', "r", encoding="utf8") as f:
        html = markdown.markdown(f.read())
        return html


if __name__ == "__main__":
    app.run(debug=True, port=5000)
