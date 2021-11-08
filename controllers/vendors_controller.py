from flask import Flask, render_template, request, redirect, Blueprint
from repositories import vendor_repository

# products blueprint
vendors_blueprint = Blueprint("vendors", __name__)

# vendors
@vendors_blueprint.route("/vendors", methods=["GET"])
def vendors():
    all_vendors = vendor_repository.select_all()
    return render_template("vendors/index.html", heading="Vendors", all_vendors=all_vendors)