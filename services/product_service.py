products = []

def create_product(name, price):
    product = {"id": len(products)+1, "name": name, "price": price}
    products.append(product)
    return product

def get_all_products():
    return products
