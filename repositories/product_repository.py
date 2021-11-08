from db.run_sql import run_sql
from models.product import Product
from repositories import vendor_repository

def save(product):
    sql = "INSERT INTO products (name, description, stock_quantity, buying_cost, selling_price, vendor_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.name, product.description, product.stock_quantity, product.buying_cost, product.selling_price, product.vendor.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    product.id = id

def select_by_id(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]
    if results is not None:
        vendor = vendor_repository.select_by_id(results["vendor_id"])
        product = Product(results["name"], results["description"], results["stock_quantity"], results["buying_cost"], results["selling_price"], vendor)
    return product

def select_all():
    products = []
    sql = "SELECT * FROM products"
    results = run_sql(sql)
    for row in results:
        vendor = vendor_repository.select_by_id(row["vendor_id"])
        product = Product(row["name"], row["description"], row["stock_quantity"], row["buying_cost"], row["selling_price"], vendor, row["id"])
        products.append(product)
    return products

def delete_by_id(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

def update(product):
    sql = "UPDATE products SET (name, description, stock_quantity, buying_cost, selling_price, vendor_id) VALUES (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [product.name, product.description, product.stock_quantity, product.buying_cost, product.selling_price, product.vendor.id]
    run_sql(sql, values)
