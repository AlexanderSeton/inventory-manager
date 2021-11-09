class Product:
    def __init__(self, name, description, stock_quantity, buying_cost, selling_price, vendor, id=None):
        self.name = name
        self.description = description
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.vendor = vendor
        self.id = id

    def calculate_profit(self):
        profit = (((self.selling_price - self.buying_cost) / self.selling_price) * 100)
        return profit
