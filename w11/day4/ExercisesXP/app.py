# Exercises XP
# Marketplace
import json

from flask import Flask, render_template, url_for

app = Flask(__name__)


def load_database():
    with open('product_db.json', 'r') as f:
        data = json.load(f)
    return data


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/products')
def products():
    info = load_database()
    return render_template('products.html', products=info)


@app.route('/products/<product_id>')
def prod_details(product_id):
    info = load_database()
    return render_template('product_details.html', products=info, product_id=product_id)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
