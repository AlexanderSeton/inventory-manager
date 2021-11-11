from re import X
from flask import Flask, render_template
from numpy.core.fromnumeric import prod
from controllers.products_controller import products_blueprint
from controllers.vendors_controller import vendors_blueprint
from repositories import product_repository
from repositories import vendor_repository
from models.product import Product
from matplotlib import pyplot as plt
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib
import seaborn
from flask import send_file
from flask.helpers import url_for

app = Flask(__name__)

app.register_blueprint(products_blueprint)
app.register_blueprint(vendors_blueprint)

@app.route("/")
def home():
    # store overview figures
    all_products = product_repository.select_all()
    all_vendors = vendor_repository.select_all()
    number_product_types = len(all_products)
    number_all_units = 0
    for product in all_products:
        number_all_units += product.stock_quantity
    number_vendors = len(all_vendors)
    total_stock_value = 0
    for product in all_products:
        total_stock_value += product.selling_price * product.stock_quantity
    return render_template("index.html", heading="Dashboard", number_product_types=number_product_types, number_all_units=number_all_units, number_vendors=number_vendors, total_stock_value=total_stock_value)

@app.route("/piechart/<rank>")
def piechart(rank):
    matplotlib.rc_file_defaults()
    rank = int(rank)
    # get 3 most profitable products
    all_products = product_repository.select_all()
    most_profitable_product = all_products[0]
    for product in all_products:
        temp_profit = product.calculate_profit()
        if temp_profit > most_profitable_product.calculate_profit():
            most_profitable_product = product
    product = most_profitable_product
    # creating the pie chart
    plt.switch_backend("Agg")
    fig, ax = plt.subplots(figsize=(3, 3))
    data = [(product.selling_price - product.buying_cost), product.buying_cost]
    labels = [f"Profit: £{(product.selling_price - product.buying_cost)}", f"Cost: £{product.buying_cost}"]
    colors = seaborn.color_palette("Blues")
    plt.pie(x=data, labels=labels, colors=colors, autopct="%.0f%%")
    ax.set_title(f"Product: {product.name}")
    canvas = FigureCanvas(fig)
    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype="img/png")

@app.route("/barchart")
def barchart():
    # get three products with the lowest stock levels
    all_products = product_repository.select_all()
    print("\n\n\ALL LOWEST STOCK ITEMS: ", all_products)
    lowest_stock_three = []
    lowest_stock_three = all_products[0].get_three_lowest_stock(all_products)
    print("\n\n\nTHREE LOWEST STOCK ITEMS: ", lowest_stock_three)
    # create bar chart
    # plt.switch_backend("Agg")
    fig, ax = plt.subplots(figsize=(7, 3))
    x = [product.name for product in lowest_stock_three]
    y = [product.stock_quantity for product in lowest_stock_three]
    plt.bar(x, y)
    ax.set_title(f"3 Lowest Stock Products")
    canvas = FigureCanvas(fig)
    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype="img/png")

if __name__ == "__main__":
    app.run(debug=True)
