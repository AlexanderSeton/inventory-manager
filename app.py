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

@app.route("/visualize")
def visualize():
    # get 3 most profitable products
    all_products = product_repository.select_all()
    most_profitable_products = []
    for i in range(3):
        most_prof = all_products[0]
        for product in all_products:
            product_profit = product.calculate_profit()
            if product_profit > most_prof.calculate_profit() and product not in most_profitable_products:
                most_prof = product
        most_profitable_products.append(most_prof)
    
    # creating the pie chart
    plt.switch_backend("Agg")
    fig, ax=plt.subplots(figsize=(3, 3))
    data = [(most_profitable_products[0].selling_price - most_profitable_products[0].buying_cost), most_profitable_products[0].buying_cost]
    labels = ["Profit", "Cost"]
    colors = seaborn.color_palette("Blues")
    plt.pie(x=data, labels=labels, colors=colors, autopct="%.0f%%")
    ax.set_title(f"{most_profitable_products[0].name}")
    canvas = FigureCanvas(fig)
    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype="img/png")





if __name__ == "__main__":
    app.run(debug=True)
