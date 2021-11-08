from flask import Flask, render_template
from controllers.products_controller import products_blueprint
from controllers.vendors_controller import vendors_blueprint

app = Flask(__name__)

app.register_blueprint(products_blueprint)
app.register_blueprint(vendors_blueprint)

@app.route("/")
def home():
    return render_template("index.html", heading="Dashboard")

if __name__ == "__main__":
    app.run(debug=True)
