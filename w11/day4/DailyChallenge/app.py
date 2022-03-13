from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('homePage.html', color='white')


@app.route('/blue')
def blue():
    return render_template('homePage.html', color='blue')


@app.route('/red')
def red():
    return render_template('homePage.html', color='red')


@app.route('/green')
def green():
    return render_template('homePage.html', color='green')


@app.route('/yellow')
def yellow():
    return render_template('homePage.html', color='yellow')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
