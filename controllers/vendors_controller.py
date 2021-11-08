from flask import Flask, render_template, request, redirect, Blueprint
from models.vendor import Vendor
from repositories import vendor_repository

# vendors blueprint
vendors_blueprint = Blueprint("vendors", __name__)

# action: index
# display vendors
@vendors_blueprint.route("/vendors", methods=["GET"])
def vendors():
    all_vendors = vendor_repository.select_all()
    return render_template("vendors/index.html", heading="Vendors", all_vendors=all_vendors)

# action: new
# display new vendor form 
@vendors_blueprint.route("/vendors/new", methods=["GET"])
def new_vendor():
    return render_template("vendors/new.html", heading="Add Vendor")

# action: create
# create the new product and add to database
@vendors_blueprint.route("/vendors", methods=["POST"])
def add_vendor():
    print("\n\n\n\n\n\n\n\n\n\nREQUEST FORM :", request.form)
    name = request.form["name"]
    if "active" in request.form:
        active = True
    else:
        active = False
    vendor = Vendor(name, active)
    vendor_repository.save(vendor)
    return redirect("/vendors")
