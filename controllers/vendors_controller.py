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
    name = request.form["name"]
    if "active" in request.form:
        active = True
    else:
        active = False
    vendor = Vendor(name, active)
    vendor_repository.save(vendor)
    return redirect("/vendors")

# action: edit
# display edit product page
@vendors_blueprint.route("/vendors/<id>/edit", methods=["GET"])
def edit_vendor(id):
    vendor = vendor_repository.select_by_id(id)
    print("VENDOR FROM SELCT CONTROLLER: ", vendor.__dict__)
    return render_template("vendors/edit.html", vendor=vendor)

# action: update
# update the product on the databse
@vendors_blueprint.route("/vendors/<id>", methods=["POST"])
def update_vendor(id):
    name = request.form["name"]
    if "active" in request.form:
        active = True
    else:
        active = False
    vendor = Vendor(name, active, id)
    vendor_repository.update(vendor)
    return redirect("/vendors")
