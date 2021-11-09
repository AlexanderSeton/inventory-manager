from flask import Flask, render_template, request, redirect, Blueprint
from models.product import Product
from repositories import product_repository
from repositories import vendor_repository

# products blueprint
products_blueprint = Blueprint("products", __name__)

# action: index
# display inventory
@products_blueprint.route("/products", methods=["GET"])
def products():
    all_products = product_repository.select_all()
    all_vendors = vendor_repository.select_all()
    return render_template("products/index.html", heading="Inventory", all_products=all_products, all_vendors=all_vendors)

# action: new
# display new product page
@products_blueprint.route("/products/new", methods=["GET"])
def new_product():
    all_vendors = vendor_repository.select_all()
    return render_template("products/new.html", heading="Add Product", all_vendors=all_vendors)

# action: create
# create the new product and add to database
@products_blueprint.route("/products", methods=["POST"])
def add_product():
    name = request.form["name"]
    description = request.form["description"]
    stock_quantity = request.form["stock_quantity"]
    buying_cost = request.form["buying_cost"]
    selling_price = request.form["selling_price"]
    vendor = vendor_repository.select_by_id(request.form["vendor_id"])
    product = Product(name, description, stock_quantity, buying_cost, selling_price, vendor)
    product_repository.save(product)
    return redirect("/products")

# action: edit
# display edit product page
@products_blueprint.route("/products/<id>/edit", methods=["GET"])
def edit_product(id):
    product = product_repository.select_by_id(id)
    all_vendors = vendor_repository.select_all()
    return render_template("products/edit.html", heading="Edit Product", product=product, all_vendors=all_vendors)

# action: update
# update the product on the databse
@products_blueprint.route("/products/<id>", methods=["POST"])
def update_product(id):
    name = request.form["name"]
    description = request.form["description"]
    stock_quantity = request.form["stock_quantity"]
    buying_cost = request.form["buying_cost"]
    selling_price = request.form["selling_price"]
    vendor = vendor_repository.select_by_id(request.form["vendor_id"])
    product = Product(name, description, stock_quantity, buying_cost, selling_price, vendor, id)
    product_repository.update(product)
    return redirect("/products")

# action: show
# show an individual product

