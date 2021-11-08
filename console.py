import pdb
from models.vendor import Vendor
from models.product import Product
from repositories import vendor_repository
from repositories import product_repository

# delete all
product_repository.delete_all()
vendor_repository.delete_all()

# vendors
vendor1 = Vendor("vendor1")
vendor_repository.save(vendor1)

# products
product1 = Product("product1", "Test product", 120, 2.50, 3.75, vendor1)
product_repository.save(product1)

# print
vendors = vendor_repository.select_all()
for vendor in vendors:
    print("vtest", vendor.__dict__)
products = product_repository.select_all()
for product in products:
    print("ptest", product.__dict__)

# set trace
pdb.set_trace()
