from flask import Flask, render_template
from controllers.products_controller import products_blueprint
from controllers.vendors_controller import vendors_blueprint
from repositories import product_repository
from repositories import vendor_repository

app = Flask(__name__)

app.register_blueprint(products_blueprint)
app.register_blueprint(vendors_blueprint)

@app.route("/")
def home():
    all_products = product_repository.select_all()
    all_vendors = vendor_repository.select_all()
    number_product_types = len(all_products)
    number_all_products = 0
    for product in all_products:
        number_all_products += product.stock_quantity
    number_vendors = len(all_vendors)
    total_stock_value = 0
    for product in all_products:
        total_stock_value += product.selling_price * product.stock_quantity
    return render_template("index.html", heading="Dashboard", number_product_types=number_product_types, number_all_products=number_all_products, number_vendors=number_vendors, total_stock_value=total_stock_value)

if __name__ == "__main__":
    app.run(debug=True)
