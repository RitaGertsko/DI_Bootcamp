import json

def retrieve_all_products():
    with open('products.json', 'r') as f:
        all_products = json.load(f)
    return all_products


def retrieve_requested_product(product_id):
    all_products_list = retrieve_all_products()
    for product in all_products_list:
        if product["ProductId"] == product_id:
            return product
