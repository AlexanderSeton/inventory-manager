from db.run_sql import run_sql
from models.vendor import Vendor

def save(vendor):
    sql = "INSERT INTO vendors (name, active) VALUES (%s, %s) RETURNING *"
    values = [vendor.name, vendor.active]
    results = run_sql(sql, values)
    print("RESULTS:    ", results)
    id = results[0]["id"]
    vendor.id = id

def select_by_id(id):
    vendor = None
    sql = "SELECT * FROM vendors WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]
    if results is not None:
        vendor = Vendor(results["name"], results["active"], results["id"])
    return vendor

def select_all():
    vendors = []
    sql = "SELECT * FROM vendors"
    results = run_sql(sql)
    for row in results:
        vendor = Vendor(row["name"], row["active"], row["id"])
        vendors.append(vendor)
    return vendors

def delete_by_id(id):
    sql = "DELETE FROM vendors WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM vendors"
    run_sql(sql)

def update(vendor):
    sql = "UPDATE vendors SET (name, active) = (%s, %s) WHERE id = %s"
    values = [vendor.name, vendor.active, vendor.id]
    run_sql(sql, values)
