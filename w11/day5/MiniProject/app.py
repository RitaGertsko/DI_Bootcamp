# Mini Project : Shopping Cart Site

from products_data import retrieve_all_products, retrieve_requested_product
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

cart_items = []


@app.route('/')
def homepage():
    return render_template('index.html', title='Homepage')


@app.route('/products')
def products():
    return render_template('products.html', title='Products', products=retrieve_all_products())


@app.route('/products/<product_id>')
def product_info(product_id):
    required_product = retrieve_requested_product(product_id)
    return render_template('product_info.html', product=required_product, title=required_product["Name"])


@app.route('/cart')
def go_to_cart():
    total_price = 0
    for product in cart_items:
        total_price += product['Price']
    return render_template('cart.html', title='Cart', cart_items=cart_items, len=len(cart_items),
                           total_price=total_price)


@app.route('/add_product_to_cart/<product_id>')
def add_product_to_cart(product_id):
    product = retrieve_requested_product(product_id)
    cart_items.append(product)
    return redirect(url_for('go_to_cart'))


@app.route('/delete_product_from_cart/<product_id>')
def delete_product_from_cart(product_id):
    product = retrieve_requested_product(product_id)
    cart_items.remove(product)
    return redirect(url_for('go_to_cart'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
